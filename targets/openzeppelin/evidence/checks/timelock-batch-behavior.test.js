const { expect } = require('chai');
const { ethers } = require('hardhat');
const { time } = require('@nomicfoundation/hardhat-network-helpers');

describe('TimelockController batch behavior', function () {
  async function scheduleBatch(secondCall) {
    const [proposer, caller] = await ethers.getSigners();
    const delay = 3600;
    const timelock = await ethers.deployContract('TimelockController', [
      delay,
      [proposer.address],
      [ethers.ZeroAddress],
      ethers.ZeroAddress,
    ]);
    const receiver = await ethers.deployContract('CallReceiverMock');
    const targets = [receiver.target, receiver.target];
    const values = [1n, 0n];
    const payloads = ['mockFunction', secondCall].map(name => receiver.interface.encodeFunctionData(name));
    const args = [targets, values, payloads, ethers.ZeroHash, ethers.ZeroHash];
    const operationId = await timelock.hashOperationBatch(...args);

    await timelock.connect(proposer).scheduleBatch(...args, delay);
    const readyAt = await timelock.getTimestamp(operationId);
    return { proposer, caller, timelock, receiver, args, operationId, readyAt };
  }

  it('executes an authorized public batch exactly at its scheduled timestamp', async function () {
    const { caller, timelock, receiver, args, operationId, readyAt } = await scheduleBatch('mockFunction');
    expect(await timelock.hasRole(await timelock.EXECUTOR_ROLE(), caller.address)).to.equal(false);
    expect(await timelock.isOperationReady(operationId)).to.equal(false);

    await time.setNextBlockTimestamp(readyAt);
    const transaction = await timelock.connect(caller).executeBatch(...args, { value: 1n });
    await expect(transaction).to.emit(timelock, 'CallExecuted').withArgs(operationId, 0n, receiver.target, 1n, args[2][0]);
    await expect(transaction).to.emit(timelock, 'CallExecuted').withArgs(operationId, 1n, receiver.target, 0n, args[2][1]);
    const receipt = await transaction.wait();
    expect(BigInt((await ethers.provider.getBlock(receipt.blockNumber)).timestamp)).to.equal(readyAt);
    expect(await timelock.isOperationDone(operationId)).to.equal(true);
    expect(await ethers.provider.getBalance(receiver)).to.equal(1n);
  });

  it('clears a cancelled batch reservation', async function () {
    const { proposer, timelock, operationId } = await scheduleBatch('mockFunction');
    await expect(timelock.connect(proposer).cancel(operationId)).to.emit(timelock, 'Cancelled').withArgs(operationId);
    expect(await timelock.getTimestamp(operationId)).to.equal(0n);
    expect(await timelock.isOperation(operationId)).to.equal(false);
  });

  it('keeps the batch ready and rolls back effects when a receiver rejects a call', async function () {
    const { caller, timelock, receiver, args, operationId, readyAt } =
      await scheduleBatch('mockFunctionRevertsNoReason');
    await time.increaseTo(readyAt);
    const beforeBlock = await ethers.provider.getBlockNumber();

    await expect(timelock.connect(caller).executeBatch(...args, { value: 1n, gasLimit: 1_000_000 }))
      .to.be.revertedWithCustomError(timelock, 'FailedCall');

    expect(await timelock.getTimestamp(operationId)).to.equal(readyAt);
    expect(await timelock.isOperationReady(operationId)).to.equal(true);
    expect(await timelock.isOperationDone(operationId)).to.equal(false);
    expect(await ethers.provider.getBalance(timelock)).to.equal(0n);
    expect(await ethers.provider.getBalance(receiver)).to.equal(0n);
    expect(await timelock.queryFilter(timelock.filters.CallExecuted(operationId), beforeBlock + 1)).to.deep.equal([]);
    expect(await receiver.queryFilter(receiver.filters.MockFunctionCalled(), beforeBlock + 1)).to.deep.equal([]);
  });
});
