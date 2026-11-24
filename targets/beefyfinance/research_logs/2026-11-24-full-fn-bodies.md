# 2026-11-24 — Complete Function Bodies for Hypothesis Audit

## `contracts/archive/infra/FlatBeefyZap.sol`

### `beefInETH` (L842–L848)
```solidity
 842:     function beefInETH (address beefyVault, uint256 tokenAmountOutMin) external payable {
 843:         require(msg.value >= minimumAmount, 'Beefy: Insignificant input amount');
 844: 
 845:         IWETH(WETH).deposit{value: msg.value}();
 846: 
 847:         _swapAndStake(beefyVault, tokenAmountOutMin, WETH);
 848:     }
```

### `beefIn` (L850–L857)
```solidity
 850:     function beefIn (address beefyVault, uint256 tokenAmountOutMin, address tokenIn, uint256 tokenInAmount) external {
 851:         require(tokenInAmount >= minimumAmount, 'Beefy: Insignificant input amount');
 852:         require(IERC20(tokenIn).allowance(msg.sender, address(this)) >= tokenInAmount, 'Beefy: Input token is not approved');
 853: 
 854:         IERC20(tokenIn).safeTransferFrom(msg.sender, address(this), tokenInAmount);
 855: 
 856:         _swapAndStake(beefyVault, tokenAmountOutMin, tokenIn);
 857:     }
```

### `beefOut` (L859–L876)
```solidity
 859:     function beefOut (address beefyVault, uint256 withdrawAmount) external {
 860:         (IBeefyVaultV6 vault, IUniswapV2Pair pair) = _getVaultPair(beefyVault);
 861: 
 862:         IERC20(beefyVault).safeTransferFrom(msg.sender, address(this), withdrawAmount);
 863:         vault.withdraw(withdrawAmount);
 864: 
 865:         if (pair.token0() != WETH && pair.token1() != WETH) {
 866:             return _removeLiqudity(address(pair), msg.sender);
 867:         }
 868: 
 869:         _removeLiqudity(address(pair), address(this));
 870: 
 871:         address[] memory tokens = new address[](2);
 872:         tokens[0] = pair.token0();
 873:         tokens[1] = pair.token1();
 874: 
 875:         _returnAssets(tokens);
 876:     }
```

### `beefOutAndSwap` (L878–L897)
```solidity
 878:     function beefOutAndSwap(address beefyVault, uint256 withdrawAmount, address desiredToken, uint256 desiredTokenOutMin) external {
 879:         (IBeefyVaultV6 vault, IUniswapV2Pair pair) = _getVaultPair(beefyVault);
 880:         address token0 = pair.token0();
 881:         address token1 = pair.token1();
 882:         require(token0 == desiredToken || token1 == desiredToken, 'Beefy: desired token not present in liqudity pair');
 883: 
 884:         vault.safeTransferFrom(msg.sender, address(this), withdrawAmount);
 885:         vault.withdraw(withdrawAmount);
 886:         _removeLiqudity(address(pair), address(this));
 887: 
 888:         address swapToken = token1 == desiredToken ? token0 : token1;
 889:         address[] memory path = new address[](2);
 890:         path[0] = swapToken;
 891:         path[1] = desiredToken;
 892: 
 893:         _approveTokenIfNeeded(path[0], address(router));
 894:         router.swapExactTokensForTokens(IERC20(swapToken).balanceOf(address(this)), desiredTokenOutMin, path, address(this), block.timestamp);
 895: 
 896:         _returnAssets(path);
 897:     }
```

### `_removeLiqudity` (L899–L905)
```solidity
 899:     function _removeLiqudity(address pair, address to) private {
 900:         IERC20(pair).safeTransfer(pair, IERC20(pair).balanceOf(address(this)));
 901:         (uint256 amount0, uint256 amount1) = IUniswapV2Pair(pair).burn(to);
 902: 
 903:         require(amount0 >= minimumAmount, 'UniswapV2Router: INSUFFICIENT_A_AMOUNT');
 904:         require(amount1 >= minimumAmount, 'UniswapV2Router: INSUFFICIENT_B_AMOUNT');
 905:     }
```

### `_getVaultPair` (L907–L911)
```solidity
 907:     function _getVaultPair (address beefyVault) private view returns (IBeefyVaultV6 vault, IUniswapV2Pair pair) {
 908:         vault = IBeefyVaultV6(beefyVault);
 909:         pair = IUniswapV2Pair(vault.want());
 910:         require(pair.factory() == router.factory(), 'Beefy: Incompatible liquidity pair factory');
 911:     }
```

### `_swapAndStake` (L913–L947)
```solidity
 913:     function _swapAndStake(address beefyVault, uint256 tokenAmountOutMin, address tokenIn) private {
 914:         (IBeefyVaultV6 vault, IUniswapV2Pair pair) = _getVaultPair(beefyVault);
 915: 
 916:         (uint256 reserveA, uint256 reserveB,) = pair.getReserves();
 917:         require(reserveA > minimumAmount && reserveB > minimumAmount, 'Beefy: Liquidity pair reserves too low');
 918: 
 919:         bool isInputA = pair.token0() == tokenIn;
 920:         require(isInputA || pair.token1() == tokenIn, 'Beefy: Input token not present in liqudity pair');
 921: 
 922:         address[] memory path = new address[](2);
 923:         path[0] = tokenIn;
 924:         path[1] = isInputA ? pair.token1() : pair.token0();
 925: 
 926:         uint256 fullInvestment = IERC20(tokenIn).balanceOf(address(this));
 927:         uint256 swapAmountIn;
 928:         if (isInputA) {
 929:             swapAmountIn = _getSwapAmount(fullInvestment, reserveA, reserveB);
 930:         } else {
 931:             swapAmountIn = _getSwapAmount(fullInvestment, reserveB, reserveA);
 932:         }
 933: 
 934:         _approveTokenIfNeeded(path[0], address(router));
 935:         uint256[] memory swapedAmounts = router
 936:             .swapExactTokensForTokens(swapAmountIn, tokenAmountOutMin, path, address(this), block.timestamp);
 937: 
 938:         _approveTokenIfNeeded(path[1], address(router));
 939:         (,, uint256 amountLiquidity) = router
 940:             .addLiquidity(path[0], path[1], fullInvestment.sub(swapedAmounts[0]), swapedAmounts[1], 1, 1, address(this), block.timestamp);
 941: 
 942:         _approveTokenIfNeeded(address(pair), address(vault));
 943:         vault.deposit(amountLiquidity);
 944: 
 945:         vault.safeTransfer(msg.sender, vault.balanceOf(address(this)));
 946:         _returnAssets(path);
 947:     }
```

### `_returnAssets` (L949–L963)
```solidity
 949:     function _returnAssets(address[] memory tokens) private {
 950:         uint256 balance;
 951:         for (uint256 i; i < tokens.length; i++) {
 952:             balance = IERC20(tokens[i]).balanceOf(address(this));
 953:             if (balance > 0) {
 954:                 if (tokens[i] == WETH) {
 955:                     IWETH(WETH).withdraw(balance);
 956:                     (bool success,) = msg.sender.call{value: balance}(new bytes(0));
 957:                     require(success, 'Beefy: ETH transfer failed');
 958:                 } else {
 959:                     IERC20(tokens[i]).safeTransfer(msg.sender, balance);
 960:                 }
 961:             }
 962:         }
 963:     }
```

### `_getSwapAmount` (L965–L970)
```solidity
 965:     function _getSwapAmount(uint256 investmentA, uint256 reserveA, uint256 reserveB) private view returns (uint256 swapAmount) {
 966:         uint256 halfInvestment = investmentA / 2;
 967:         uint256 nominator = router.getAmountOut(halfInvestment, reserveA, reserveB);
 968:         uint256 denominator = router.quote(halfInvestment, reserveA.add(halfInvestment), reserveB.sub(nominator));
 969:         swapAmount = investmentA.sub(Babylonian.sqrt(halfInvestment * halfInvestment * nominator / denominator));
 970:     }
```

### `_approveTokenIfNeeded` (L992–L996)
```solidity
 992:     function _approveTokenIfNeeded(address token, address spender) private {
 993:         if (IERC20(token).allowance(address(this), spender) == 0) {
 994:             IERC20(token).safeApprove(spender, type(uint).max);
 995:         }
 996:     }
```

## `contracts/archive/strategies/Cometh/StrategyMultiRewardsPolygonLP.sol`

### `deposit` (L159–L171)
```solidity
 159:     function deposit() public whenNotPaused {
 160: 
 161:         uint256 wantBal = IERC20(want).balanceOf(address(this));
 162: 
 163: 
 164: 
 165:         if (wantBal > 0) {
 166: 
 167:             IRewardPool(rewardPool).stake(wantBal);
 168: 
 169:         }
 170: 
 171:     }
```

### `withdraw` (L175–L215)
```solidity
 175:     function withdraw(uint256 _amount) external {
 176: 
 177:         require(msg.sender == vault, "!vault");
 178: 
 179: 
 180: 
 181:         uint256 wantBal = IERC20(want).balanceOf(address(this));
 182: 
 183: 
 184: 
 185:         if (wantBal < _amount) {
 186: 
 187:             IRewardPool(rewardPool).withdraw(_amount.sub(wantBal));
 188: 
 189:             wantBal = IERC20(want).balanceOf(address(this));
 190: 
 191:         }
 192: 
 193: 
 194: 
 195:         if (wantBal > _amount) {
 196: 
 197:             wantBal = _amount;
 198: 
 199:         }
 200: 
 201: 
 202: 
 203:         if (tx.origin == owner() || paused()) {
 204: 
 205:             IERC20(want).safeTransfer(vault, wantBal);
 206: 
 207:         } else {
 208: 
 209:             uint256 withdrawalFee = wantBal.mul(WITHDRAWAL_FEE_CAP).div(WITHDRAWAL_MAX);
 210: 
 211:             IERC20(want).safeTransfer(vault, wantBal.sub(withdrawalFee));
 212: 
 213:         }
 214: 
 215:     }
```

### `harvest` (L221–L235)
```solidity
 221:     function harvest() external whenNotPaused {
 222: 
 223:         IRewardPool(rewardPool).getReward();
 224: 
 225:         chargeFees();
 226: 
 227:         addLiquidity();
 228: 
 229:         deposit();
 230: 
 231: 
 232: 
 233:         emit StratHarvest(msg.sender);
 234: 
 235:     }
```

### `chargeFees` (L241–L275)
```solidity
 241:     function chargeFees() internal {
 242: 
 243:         uint256 toOutput = IERC20(secondOutput).balanceOf(address(this));
 244: 
 245:         IUniswapRouterETH(unirouter).swapExactTokensForTokens(toOutput, 0, secondOutputToOutputRoute, address(this), now);
 246: 
 247:         
 248: 
 249:         uint256 toMatic = IERC20(output).balanceOf(address(this)).mul(45).div(1000);
 250: 
 251:         IUniswapRouterETH(unirouter).swapExactTokensForTokens(toMatic, 0, outputToMaticRoute, address(this), now);
 252: 
 253: 
 254: 
 255:         uint256 maticBal = IERC20(matic).balanceOf(address(this));
 256: 
 257: 
 258: 
 259:         uint256 callFeeAmount = maticBal.mul(callFee).div(MAX_FEE);
 260: 
 261:         IERC20(matic).safeTransfer(tx.origin, callFeeAmount);
 262: 
 263: 
 264: 
 265:         uint256 beefyFeeAmount = maticBal.mul(beefyFee).div(MAX_FEE);
 266: 
 267:         IERC20(matic).safeTransfer(beefyFeeRecipient, beefyFeeAmount);
 268: 
 269: 
 270: 
 271:         uint256 strategistFee = maticBal.mul(STRATEGIST_FEE).div(MAX_FEE);
 272: 
 273:         IERC20(matic).safeTransfer(strategist, strategistFee);
 274: 
 275:     }
```

### `addLiquidity` (L281–L309)
```solidity
 281:     function addLiquidity() internal {
 282: 
 283:         uint256 outputHalf = IERC20(output).balanceOf(address(this)).div(2);
 284: 
 285: 
 286: 
 287:         if (lpToken0 != output) {
 288: 
 289:             IUniswapRouterETH(unirouter).swapExactTokensForTokens(outputHalf, 0, outputToLp0Route, address(this), now);
 290: 
 291:         }
 292: 
 293: 
 294: 
 295:         if (lpToken1 != output) {
 296: 
 297:             IUniswapRouterETH(unirouter).swapExactTokensForTokens(outputHalf, 0, outputToLp1Route, address(this), now);
 298: 
 299:         }
 300: 
 301: 
 302: 
 303:         uint256 lp0Bal = IERC20(lpToken0).balanceOf(address(this));
 304: 
 305:         uint256 lp1Bal = IERC20(lpToken1).balanceOf(address(this));
 306: 
 307:         IUniswapRouterETH(unirouter).addLiquidity(lpToken0, lpToken1, lp0Bal, lp1Bal, 1, 1, address(this), now);
 308: 
 309:     }
```

### `balanceOf` (L315–L319)
```solidity
 315:     function balanceOf() public view returns (uint256) {
 316: 
 317:         return balanceOfWant().add(balanceOfPool());
 318: 
 319:     }
```

### `retireStrat` (L345–L359)
```solidity
 345:     function retireStrat() external {
 346: 
 347:         require(msg.sender == vault, "!vault");
 348: 
 349: 
 350: 
 351:         IRewardPool(rewardPool).withdraw(balanceOfPool());
 352: 
 353: 
 354: 
 355:         uint256 wantBal = IERC20(want).balanceOf(address(this));
 356: 
 357:         IERC20(want).transfer(vault, wantBal);
 358: 
 359:     }
```

### `panic` (L365–L371)
```solidity
 365:     function panic() public onlyManager {
 366: 
 367:         pause();
 368: 
 369:         IRewardPool(rewardPool).withdraw(balanceOfPool());
 370: 
 371:     }
```

## `contracts/archive/strategies/Cometh/StrategyRewardPoolPolygonLP.sol`

### `deposit` (L147–L159)
```solidity
 147:     function deposit() public whenNotPaused {
 148: 
 149:         uint256 wantBal = IERC20(want).balanceOf(address(this));
 150: 
 151: 
 152: 
 153:         if (wantBal > 0) {
 154: 
 155:             IRewardPool(rewardPool).stake(wantBal);
 156: 
 157:         }
 158: 
 159:     }
```

### `withdraw` (L163–L203)
```solidity
 163:     function withdraw(uint256 _amount) external {
 164: 
 165:         require(msg.sender == vault, "!vault");
 166: 
 167: 
 168: 
 169:         uint256 wantBal = IERC20(want).balanceOf(address(this));
 170: 
 171: 
 172: 
 173:         if (wantBal < _amount) {
 174: 
 175:             IRewardPool(rewardPool).withdraw(_amount.sub(wantBal));
 176: 
 177:             wantBal = IERC20(want).balanceOf(address(this));
 178: 
 179:         }
 180: 
 181: 
 182: 
 183:         if (wantBal > _amount) {
 184: 
 185:             wantBal = _amount;
 186: 
 187:         }
 188: 
 189: 
 190: 
 191:         if (tx.origin == owner() || paused()) {
 192: 
 193:             IERC20(want).safeTransfer(vault, wantBal);
 194: 
 195:         } else {
 196: 
 197:             uint256 withdrawalFee = wantBal.mul(WITHDRAWAL_FEE_CAP).div(WITHDRAWAL_MAX);
 198: 
 199:             IERC20(want).safeTransfer(vault, wantBal.sub(withdrawalFee));
 200: 
 201:         }
 202: 
 203:     }
```

### `harvest` (L209–L223)
```solidity
 209:     function harvest() external whenNotPaused {
 210: 
 211:         IRewardPool(rewardPool).getReward();
 212: 
 213:         chargeFees();
 214: 
 215:         addLiquidity();
 216: 
 217:         deposit();
 218: 
 219: 
 220: 
 221:         emit StratHarvest(msg.sender);
 222: 
 223:     }
```

### `chargeFees` (L229–L257)
```solidity
 229:     function chargeFees() internal {
 230: 
 231:         uint256 toMatic = IERC20(output).balanceOf(address(this)).mul(45).div(1000);
 232: 
 233:         IUniswapRouterETH(unirouter).swapExactTokensForTokens(toMatic, 0, outputToMaticRoute, address(this), now);
 234: 
 235: 
 236: 
 237:         uint256 maticBal = IERC20(matic).balanceOf(address(this));
 238: 
 239: 
 240: 
 241:         uint256 callFeeAmount = maticBal.mul(callFee).div(MAX_FEE);
 242: 
 243:         IERC20(matic).safeTransfer(tx.origin, callFeeAmount);
 244: 
 245: 
 246: 
 247:         uint256 beefyFeeAmount = maticBal.mul(beefyFee).div(MAX_FEE);
 248: 
 249:         IERC20(matic).safeTransfer(beefyFeeRecipient, beefyFeeAmount);
 250: 
 251: 
 252: 
 253:         uint256 strategistFee = maticBal.mul(STRATEGIST_FEE).div(MAX_FEE);
 254: 
 255:         IERC20(matic).safeTransfer(strategist, strategistFee);
 256: 
 257:     }
```

### `addLiquidity` (L263–L291)
```solidity
 263:     function addLiquidity() internal {
 264: 
 265:         uint256 outputHalf = IERC20(output).balanceOf(address(this)).div(2);
 266: 
 267: 
 268: 
 269:         if (lpToken0 != output) {
 270: 
 271:             IUniswapRouterETH(unirouter).swapExactTokensForTokens(outputHalf, 0, outputToLp0Route, address(this), now);
 272: 
 273:         }
 274: 
 275: 
 276: 
 277:         if (lpToken1 != output) {
 278: 
 279:             IUniswapRouterETH(unirouter).swapExactTokensForTokens(outputHalf, 0, outputToLp1Route, address(this), now);
 280: 
 281:         }
 282: 
 283: 
 284: 
 285:         uint256 lp0Bal = IERC20(lpToken0).balanceOf(address(this));
 286: 
 287:         uint256 lp1Bal = IERC20(lpToken1).balanceOf(address(this));
 288: 
 289:         IUniswapRouterETH(unirouter).addLiquidity(lpToken0, lpToken1, lp0Bal, lp1Bal, 1, 1, address(this), now);
 290: 
 291:     }
```

### `balanceOf` (L297–L301)
```solidity
 297:     function balanceOf() public view returns (uint256) {
 298: 
 299:         return balanceOfWant().add(balanceOfPool());
 300: 
 301:     }
```

### `retireStrat` (L327–L341)
```solidity
 327:     function retireStrat() external {
 328: 
 329:         require(msg.sender == vault, "!vault");
 330: 
 331: 
 332: 
 333:         IRewardPool(rewardPool).withdraw(balanceOfPool());
 334: 
 335: 
 336: 
 337:         uint256 wantBal = IERC20(want).balanceOf(address(this));
 338: 
 339:         IERC20(want).transfer(vault, wantBal);
 340: 
 341:     }
```

### `panic` (L347–L353)
```solidity
 347:     function panic() public onlyManager {
 348: 
 349:         pause();
 350: 
 351:         IRewardPool(rewardPool).withdraw(balanceOfPool());
 352: 
 353:     }
```

## `contracts/archive/vaults/BeefyVaultV6.sol`

### `balance` (L69–L71)
```solidity
  69:     function balance() public view returns (uint) {
  70:         return want().balanceOf(address(this)).add(IStrategy(strategy).balanceOf());
  71:     }
```

### `available` (L79–L81)
```solidity
  79:     function available() public view returns (uint256) {
  80:         return want().balanceOf(address(this));
  81:     }
```

### `getPricePerFullShare` (L87–L89)
```solidity
  87:     function getPricePerFullShare() public view returns (uint256) {
  88:         return totalSupply() == 0 ? 1e18 : balance().mul(1e18).div(totalSupply());
  89:     }
```

### `deposit` (L102–L117)
```solidity
 102:     function deposit(uint _amount) public nonReentrant {
 103:         strategy.beforeDeposit();
 104: 
 105:         uint256 _pool = balance();
 106:         want().safeTransferFrom(msg.sender, address(this), _amount);
 107:         earn();
 108:         uint256 _after = balance();
 109:         _amount = _after.sub(_pool); // Additional check for deflationary tokens
 110:         uint256 shares = 0;
 111:         if (totalSupply() == 0) {
 112:             shares = _amount;
 113:         } else {
 114:             shares = (_amount.mul(totalSupply())).div(_pool);
 115:         }
 116:         _mint(msg.sender, shares);
 117:     }
```

### `earn` (L123–L127)
```solidity
 123:     function earn() public {
 124:         uint _bal = available();
 125:         want().safeTransfer(address(strategy), _bal);
 126:         strategy.deposit();
 127:     }
```

### `withdraw` (L141–L157)
```solidity
 141:     function withdraw(uint256 _shares) public {
 142:         uint256 r = (balance().mul(_shares)).div(totalSupply());
 143:         _burn(msg.sender, _shares);
 144: 
 145:         uint b = want().balanceOf(address(this));
 146:         if (b < r) {
 147:             uint _withdraw = r.sub(b);
 148:             strategy.withdraw(_withdraw);
 149:             uint _after = want().balanceOf(address(this));
 150:             uint _diff = _after.sub(b);
 151:             if (_diff < _withdraw) {
 152:                 r = b.add(_diff);
 153:             }
 154:         }
 155: 
 156:         want().safeTransfer(msg.sender, r);
 157:     }
```

### `proposeStrat` (L163–L171)
```solidity
 163:     function proposeStrat(address _implementation) public onlyOwner {
 164:         require(address(this) == IStrategy(_implementation).vault(), "Proposal not valid for this Vault");
 165:         stratCandidate = StratCandidate({
 166:             implementation: _implementation,
 167:             proposedTime: block.timestamp
 168:          });
 169: 
 170:         emit NewStratCandidate(_implementation);
 171:     }
```

### `upgradeStrat` (L179–L191)
```solidity
 179:     function upgradeStrat() public onlyOwner {
 180:         require(stratCandidate.implementation != address(0), "There is no candidate");
 181:         require(stratCandidate.proposedTime.add(approvalDelay) < block.timestamp, "Delay has not passed");
 182: 
 183:         emit UpgradeStrat(stratCandidate.implementation);
 184: 
 185:         strategy.retireStrat();
 186:         strategy = IStrategy(stratCandidate.implementation);
 187:         stratCandidate.implementation = address(0);
 188:         stratCandidate.proposedTime = 5000000000;
 189: 
 190:         earn();
 191:     }
```
