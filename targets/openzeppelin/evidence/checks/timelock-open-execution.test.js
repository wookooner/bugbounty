const { expect } = require('chai');
const { ethers } = require('hardhat');
const { time } = require('@nomicfoundation/hardhat-network-helpers');

describe('TimelockController open execution configuration', function () {
  it('lets a caller execute a ready operation when execution is open', async function () {
    const [proposer, caller] = await ethers.getSigners();
    const delay = 3600;
    const timelock = await ethers.deployContract('TimelockController', [
      delay,
      [proposer.address],
      [ethers.ZeroAddress],
      ethers.ZeroAddress,
    ]);
    const receiver = await ethers.deployContract('CallReceiverMock');
    const payload = receiver.interface.encodeFunctionData('mockFunction');
    const args = [receiver.target, 0n, payload, ethers.ZeroHash, ethers.ZeroHash];
    const operationId = await timelock.hashOperation(...args);

    expect(await timelock.hasRole(await timelock.EXECUTOR_ROLE(), caller.address)).to.equal(false);
    await timelock.connect(proposer).schedule(...args, delay);
    await time.increaseTo(await timelock.getTimestamp(operationId));
    expect(await timelock.isOperationReady(operationId)).to.equal(true);

    await expect(timelock.connect(caller).execute(...args))
      .to.emit(timelock, 'CallExecuted')
      .withArgs(operationId, 0n, receiver.target, 0n, payload);
    expect(await timelock.isOperationDone(operationId)).to.equal(true);
  });
});
