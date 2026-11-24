const { expect } = require('chai');
const { ethers } = require('hardhat');

describe('AccessControlEnumerable read costs', function () {
  it('measures full-list, count, and indexed reads at four list sizes', async function () {
    const [admin] = await ethers.getSigners();
    const contract = await ethers.deployContract('$AccessControlEnumerable');
    await contract.$_grantRole(ethers.ZeroHash, admin.address);
    const role = ethers.id('BENCHMARK_ROLE');
    const members = [];
    const rows = [];

    for (const size of [0, 1, 8, 32]) {
      while (members.length < size) {
        const address = ethers.getAddress(ethers.toBeHex(1000 + members.length, 20));
        await (await contract.grantRole(role, address)).wait();
        members.push(address);
      }

      expect(await contract.getRoleMemberCount(role)).to.equal(BigInt(size));
      expect(await contract.getRoleMembers(role)).to.deep.equal(members);
      if (size > 0) {
        expect(await contract.getRoleMember(role, 0)).to.equal(members[0]);
      }
      rows.push({
        members: size,
        full_list: Number(await contract.getRoleMembers.estimateGas(role)),
        count: Number(await contract.getRoleMemberCount.estimateGas(role)),
        at_index_zero: size === 0 ? null : Number(await contract.getRoleMember.estimateGas(role, 0)),
      });
    }

    console.log('GAS_ESTIMATES ' + JSON.stringify(rows));
  });
});
