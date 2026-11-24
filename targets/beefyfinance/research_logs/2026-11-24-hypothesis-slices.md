# 2026-11-24 — Hypothesis-Oriented Function & Sink Slices

## `contracts/archive/infra/FlatBeefyZap.sol`
- All functions/constructors: `name`(L14), `symbol`(L15), `decimals`(L16), `totalSupply`(L17), `balanceOf`(L18), `allowance`(L19), `approve`(L21), `transfer`(L22), `transferFrom`(L23), `DOMAIN_SEPARATOR`(L25), `PERMIT_TYPEHASH`(L26), `nonces`(L27), `permit`(L29), `MINIMUM_LIQUIDITY`(L43), `factory`(L44), `token0`(L45), `token1`(L46), `getReserves`(L47), `price0CumulativeLast`(L48), `price1CumulativeLast`(L49), `kLast`(L50), `mint`(L52), `burn`(L53), `swap`(L54), `skim`(L55), `sync`(L56), `initialize`(L58), `sqrt`(L71), `totalSupply`(L128), `balanceOf`(L133), `transfer`(L142), `allowance`(L151), `approve`(L167), `transferFrom`(L178), `add`(L224), `sub`(L241), `sub`(L255), `mul`(L272), `div`(L298), `div`(L314), `mod`(L334), `mod`(L350), `isContract`(L382), `sendValue`(L409), `functionCall`(L435), `functionCall`(L445), `functionCallWithValue`(L460), `functionCallWithValue`(L470), `functionStaticCall`(L485), `functionStaticCall`(L495), `_verifyCallResult`(L503), `safeTransfer`(L543), `safeTransferFrom`(L547), `safeApprove`(L558), `safeIncreaseAllowance`(L569), `safeDecreaseAllowance`(L574), `_callOptionalReturn`(L585), `add`(L609), `sub`(L617), `mul`(L625), `add`(L633), `sub`(L641), `factory`(L651), `WETH`(L652), `addLiquidity`(L654), `addLiquidityETH`(L664), `removeLiquidity`(L672), `removeLiquidityETH`(L681), `removeLiquidityWithPermit`(L689), `removeLiquidityETHWithPermit`(L699), `swapExactTokensForTokens`(L708), `swapTokensForExactTokens`(L715), `swapExactETHForTokens`(L722), `swapTokensForExactETH`(L726), `swapExactTokensForETH`(L729), `swapETHForExactTokens`(L732), `quote`(L737), `getAmountOut`(L738), `getAmountIn`(L739), `getAmountsOut`(L740), `getAmountsIn`(L741), `removeLiquidityETHSupportingFeeOnTransferTokens`(L750), `removeLiquidityETHWithPermitSupportingFeeOnTransferTokens`(L758), `swapExactTokensForTokensSupportingFeeOnTransferTokens`(L768), `swapExactETHForTokensSupportingFeeOnTransferTokens`(L775), `swapExactTokensForETHSupportingFeeOnTransferTokens`(L781), `deposit`(L814), `withdraw`(L815), `deposit`(L819), `withdraw`(L820), `want`(L821), `constructor`(L833), `beefInETH`(L842), `beefIn`(L850), `beefOut`(L859), `beefOutAndSwap`(L878), `_removeLiqudity`(L899), `_getVaultPair`(L907), `_swapAndStake`(L913), `_returnAssets`(L949), `_getSwapAmount`(L965), `estimateSwap`(L972), `checkWETH`(L987), `_approveTokenIfNeeded`(L992)

### `deposit` (starts L814, showing L813–L859)
```solidity
 813: interface IWETH is IERC20 {
 814:     function deposit() external payable;
 815:     function withdraw(uint256 wad) external;
 816: }
 817: 
 818: interface IBeefyVaultV6 is IERC20 {
 819:     function deposit(uint256 amount) external;
 820:     function withdraw(uint256 shares) external;
 821:     function want() external pure returns (address);
 822: }
 823: 
 824: contract BeefyUniV2Zap {
 825:     using LowGasSafeMath for uint256;
 826:     using SafeERC20 for IERC20;
 827:     using SafeERC20 for IBeefyVaultV6;
 828: 
 829:     IUniswapV2Router02 public immutable router;
 830:     address public immutable WETH;
 831:     uint256 public constant minimumAmount = 1000;
 832: 
 833:     constructor(address _router, address _WETH) {
 834:         router = IUniswapV2Router02(_router);
 835:         WETH = _WETH;
 836:     }
 837: 
 838:     receive() external payable {
 839:         assert(msg.sender == WETH);
 840:     }
 841: 
 842:     function beefInETH (address beefyVault, uint256 tokenAmountOutMin) external payable {
 843:         require(msg.value >= minimumAmount, 'Beefy: Insignificant input amount');
 844: 
 845:         IWETH(WETH).deposit{value: msg.value}();
 846: 
 847:         _swapAndStake(beefyVault, tokenAmountOutMin, WETH);
 848:     }
 849: 
 850:     function beefIn (address beefyVault, uint256 tokenAmountOutMin, address tokenIn, uint256 tokenInAmount) external {
 851:         require(tokenInAmount >= minimumAmount, 'Beefy: Insignificant input amount');
 852:         require(IERC20(tokenIn).allowance(msg.sender, address(this)) >= tokenInAmount, 'Beefy: Input token is not approved');
 853: 
 854:         IERC20(tokenIn).safeTransferFrom(msg.sender, address(this), tokenInAmount);
 855: 
 856:         _swapAndStake(beefyVault, tokenAmountOutMin, tokenIn);
 857:     }
 858: 
 859:     function beefOut (address beefyVault, uint256 withdrawAmount) external {
```

### `withdraw` (starts L815, showing L814–L860)
```solidity
 814:     function deposit() external payable;
 815:     function withdraw(uint256 wad) external;
 816: }
 817: 
 818: interface IBeefyVaultV6 is IERC20 {
 819:     function deposit(uint256 amount) external;
 820:     function withdraw(uint256 shares) external;
 821:     function want() external pure returns (address);
 822: }
 823: 
 824: contract BeefyUniV2Zap {
 825:     using LowGasSafeMath for uint256;
 826:     using SafeERC20 for IERC20;
 827:     using SafeERC20 for IBeefyVaultV6;
 828: 
 829:     IUniswapV2Router02 public immutable router;
 830:     address public immutable WETH;
 831:     uint256 public constant minimumAmount = 1000;
 832: 
 833:     constructor(address _router, address _WETH) {
 834:         router = IUniswapV2Router02(_router);
 835:         WETH = _WETH;
 836:     }
 837: 
 838:     receive() external payable {
 839:         assert(msg.sender == WETH);
 840:     }
 841: 
 842:     function beefInETH (address beefyVault, uint256 tokenAmountOutMin) external payable {
 843:         require(msg.value >= minimumAmount, 'Beefy: Insignificant input amount');
 844: 
 845:         IWETH(WETH).deposit{value: msg.value}();
 846: 
 847:         _swapAndStake(beefyVault, tokenAmountOutMin, WETH);
 848:     }
 849: 
 850:     function beefIn (address beefyVault, uint256 tokenAmountOutMin, address tokenIn, uint256 tokenInAmount) external {
 851:         require(tokenInAmount >= minimumAmount, 'Beefy: Insignificant input amount');
 852:         require(IERC20(tokenIn).allowance(msg.sender, address(this)) >= tokenInAmount, 'Beefy: Input token is not approved');
 853: 
 854:         IERC20(tokenIn).safeTransferFrom(msg.sender, address(this), tokenInAmount);
 855: 
 856:         _swapAndStake(beefyVault, tokenAmountOutMin, tokenIn);
 857:     }
 858: 
 859:     function beefOut (address beefyVault, uint256 withdrawAmount) external {
 860:         (IBeefyVaultV6 vault, IUniswapV2Pair pair) = _getVaultPair(beefyVault);
```

### `deposit` (starts L819, showing L818–L864)
```solidity
 818: interface IBeefyVaultV6 is IERC20 {
 819:     function deposit(uint256 amount) external;
 820:     function withdraw(uint256 shares) external;
 821:     function want() external pure returns (address);
 822: }
 823: 
 824: contract BeefyUniV2Zap {
 825:     using LowGasSafeMath for uint256;
 826:     using SafeERC20 for IERC20;
 827:     using SafeERC20 for IBeefyVaultV6;
 828: 
 829:     IUniswapV2Router02 public immutable router;
 830:     address public immutable WETH;
 831:     uint256 public constant minimumAmount = 1000;
 832: 
 833:     constructor(address _router, address _WETH) {
 834:         router = IUniswapV2Router02(_router);
 835:         WETH = _WETH;
 836:     }
 837: 
 838:     receive() external payable {
 839:         assert(msg.sender == WETH);
 840:     }
 841: 
 842:     function beefInETH (address beefyVault, uint256 tokenAmountOutMin) external payable {
 843:         require(msg.value >= minimumAmount, 'Beefy: Insignificant input amount');
 844: 
 845:         IWETH(WETH).deposit{value: msg.value}();
 846: 
 847:         _swapAndStake(beefyVault, tokenAmountOutMin, WETH);
 848:     }
 849: 
 850:     function beefIn (address beefyVault, uint256 tokenAmountOutMin, address tokenIn, uint256 tokenInAmount) external {
 851:         require(tokenInAmount >= minimumAmount, 'Beefy: Insignificant input amount');
 852:         require(IERC20(tokenIn).allowance(msg.sender, address(this)) >= tokenInAmount, 'Beefy: Input token is not approved');
 853: 
 854:         IERC20(tokenIn).safeTransferFrom(msg.sender, address(this), tokenInAmount);
 855: 
 856:         _swapAndStake(beefyVault, tokenAmountOutMin, tokenIn);
 857:     }
 858: 
 859:     function beefOut (address beefyVault, uint256 withdrawAmount) external {
 860:         (IBeefyVaultV6 vault, IUniswapV2Pair pair) = _getVaultPair(beefyVault);
 861: 
 862:         IERC20(beefyVault).safeTransferFrom(msg.sender, address(this), withdrawAmount);
 863:         vault.withdraw(withdrawAmount);
 864: 
```

### `withdraw` (starts L820, showing L819–L865)
```solidity
 819:     function deposit(uint256 amount) external;
 820:     function withdraw(uint256 shares) external;
 821:     function want() external pure returns (address);
 822: }
 823: 
 824: contract BeefyUniV2Zap {
 825:     using LowGasSafeMath for uint256;
 826:     using SafeERC20 for IERC20;
 827:     using SafeERC20 for IBeefyVaultV6;
 828: 
 829:     IUniswapV2Router02 public immutable router;
 830:     address public immutable WETH;
 831:     uint256 public constant minimumAmount = 1000;
 832: 
 833:     constructor(address _router, address _WETH) {
 834:         router = IUniswapV2Router02(_router);
 835:         WETH = _WETH;
 836:     }
 837: 
 838:     receive() external payable {
 839:         assert(msg.sender == WETH);
 840:     }
 841: 
 842:     function beefInETH (address beefyVault, uint256 tokenAmountOutMin) external payable {
 843:         require(msg.value >= minimumAmount, 'Beefy: Insignificant input amount');
 844: 
 845:         IWETH(WETH).deposit{value: msg.value}();
 846: 
 847:         _swapAndStake(beefyVault, tokenAmountOutMin, WETH);
 848:     }
 849: 
 850:     function beefIn (address beefyVault, uint256 tokenAmountOutMin, address tokenIn, uint256 tokenInAmount) external {
 851:         require(tokenInAmount >= minimumAmount, 'Beefy: Insignificant input amount');
 852:         require(IERC20(tokenIn).allowance(msg.sender, address(this)) >= tokenInAmount, 'Beefy: Input token is not approved');
 853: 
 854:         IERC20(tokenIn).safeTransferFrom(msg.sender, address(this), tokenInAmount);
 855: 
 856:         _swapAndStake(beefyVault, tokenAmountOutMin, tokenIn);
 857:     }
 858: 
 859:     function beefOut (address beefyVault, uint256 withdrawAmount) external {
 860:         (IBeefyVaultV6 vault, IUniswapV2Pair pair) = _getVaultPair(beefyVault);
 861: 
 862:         IERC20(beefyVault).safeTransferFrom(msg.sender, address(this), withdrawAmount);
 863:         vault.withdraw(withdrawAmount);
 864: 
 865:         if (pair.token0() != WETH && pair.token1() != WETH) {
```

### `beefInETH` (starts L842, showing L841–L887)
```solidity
 841: 
 842:     function beefInETH (address beefyVault, uint256 tokenAmountOutMin) external payable {
 843:         require(msg.value >= minimumAmount, 'Beefy: Insignificant input amount');
 844: 
 845:         IWETH(WETH).deposit{value: msg.value}();
 846: 
 847:         _swapAndStake(beefyVault, tokenAmountOutMin, WETH);
 848:     }
 849: 
 850:     function beefIn (address beefyVault, uint256 tokenAmountOutMin, address tokenIn, uint256 tokenInAmount) external {
 851:         require(tokenInAmount >= minimumAmount, 'Beefy: Insignificant input amount');
 852:         require(IERC20(tokenIn).allowance(msg.sender, address(this)) >= tokenInAmount, 'Beefy: Input token is not approved');
 853: 
 854:         IERC20(tokenIn).safeTransferFrom(msg.sender, address(this), tokenInAmount);
 855: 
 856:         _swapAndStake(beefyVault, tokenAmountOutMin, tokenIn);
 857:     }
 858: 
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
 877: 
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
```

### `beefIn` (starts L850, showing L849–L895)
```solidity
 849: 
 850:     function beefIn (address beefyVault, uint256 tokenAmountOutMin, address tokenIn, uint256 tokenInAmount) external {
 851:         require(tokenInAmount >= minimumAmount, 'Beefy: Insignificant input amount');
 852:         require(IERC20(tokenIn).allowance(msg.sender, address(this)) >= tokenInAmount, 'Beefy: Input token is not approved');
 853: 
 854:         IERC20(tokenIn).safeTransferFrom(msg.sender, address(this), tokenInAmount);
 855: 
 856:         _swapAndStake(beefyVault, tokenAmountOutMin, tokenIn);
 857:     }
 858: 
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
 877: 
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
```

### `beefOut` (starts L859, showing L858–L904)
```solidity
 858: 
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
 877: 
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
 898: 
 899:     function _removeLiqudity(address pair, address to) private {
 900:         IERC20(pair).safeTransfer(pair, IERC20(pair).balanceOf(address(this)));
 901:         (uint256 amount0, uint256 amount1) = IUniswapV2Pair(pair).burn(to);
 902: 
 903:         require(amount0 >= minimumAmount, 'UniswapV2Router: INSUFFICIENT_A_AMOUNT');
 904:         require(amount1 >= minimumAmount, 'UniswapV2Router: INSUFFICIENT_B_AMOUNT');
```

### `beefOutAndSwap` (starts L878, showing L877–L923)
```solidity
 877: 
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
 898: 
 899:     function _removeLiqudity(address pair, address to) private {
 900:         IERC20(pair).safeTransfer(pair, IERC20(pair).balanceOf(address(this)));
 901:         (uint256 amount0, uint256 amount1) = IUniswapV2Pair(pair).burn(to);
 902: 
 903:         require(amount0 >= minimumAmount, 'UniswapV2Router: INSUFFICIENT_A_AMOUNT');
 904:         require(amount1 >= minimumAmount, 'UniswapV2Router: INSUFFICIENT_B_AMOUNT');
 905:     }
 906: 
 907:     function _getVaultPair (address beefyVault) private view returns (IBeefyVaultV6 vault, IUniswapV2Pair pair) {
 908:         vault = IBeefyVaultV6(beefyVault);
 909:         pair = IUniswapV2Pair(vault.want());
 910:         require(pair.factory() == router.factory(), 'Beefy: Incompatible liquidity pair factory');
 911:     }
 912: 
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
```

## `contracts/archive/strategies/Cometh/StrategyMultiRewardsPolygonLP.sol`
- All functions/constructors: `constructor`(L83), `deposit`(L159), `withdraw`(L175), `harvest`(L221), `chargeFees`(L241), `addLiquidity`(L281), `balanceOf`(L315), `balanceOfWant`(L325), `balanceOfPool`(L335), `retireStrat`(L345), `panic`(L365), `pause`(L375), `unpause`(L387), `_giveAllowances`(L403), `_removeAllowances`(L427)

### `deposit` (starts L159, showing L158–L204)
```solidity
 158: 
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
 172: 
 173: 
 174: 
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
```

### `withdraw` (starts L175, showing L174–L220)
```solidity
 174: 
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
 216: 
 217: 
 218: 
 219:     // compounds earnings and charges performance fee
 220: 
```

### `harvest` (starts L221, showing L220–L266)
```solidity
 220: 
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
 236: 
 237: 
 238: 
 239:     // performance fees
 240: 
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
```

### `retireStrat` (starts L345, showing L344–L390)
```solidity
 344: 
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
 360: 
 361: 
 362: 
 363:     // pauses deposits and withdraws all funds from third party systems.
 364: 
 365:     function panic() public onlyManager {
 366: 
 367:         pause();
 368: 
 369:         IRewardPool(rewardPool).withdraw(balanceOfPool());
 370: 
 371:     }
 372: 
 373: 
 374: 
 375:     function pause() public onlyManager {
 376: 
 377:         _pause();
 378: 
 379: 
 380: 
 381:         _removeAllowances();
 382: 
 383:     }
 384: 
 385: 
 386: 
 387:     function unpause() external onlyManager {
 388: 
 389:         _unpause();
 390: 
```

### `panic` (starts L365, showing L364–L410)
```solidity
 364: 
 365:     function panic() public onlyManager {
 366: 
 367:         pause();
 368: 
 369:         IRewardPool(rewardPool).withdraw(balanceOfPool());
 370: 
 371:     }
 372: 
 373: 
 374: 
 375:     function pause() public onlyManager {
 376: 
 377:         _pause();
 378: 
 379: 
 380: 
 381:         _removeAllowances();
 382: 
 383:     }
 384: 
 385: 
 386: 
 387:     function unpause() external onlyManager {
 388: 
 389:         _unpause();
 390: 
 391: 
 392: 
 393:         _giveAllowances();
 394: 
 395: 
 396: 
 397:         deposit();
 398: 
 399:     }
 400: 
 401: 
 402: 
 403:     function _giveAllowances() internal {
 404: 
 405:         IERC20(want).safeApprove(rewardPool, uint256(-1));
 406: 
 407:         IERC20(output).safeApprove(unirouter, uint256(-1));
 408: 
 409:         IERC20(secondOutput).safeApprove(unirouter, uint256(-1));
 410: 
```

## `contracts/archive/strategies/Cometh/StrategyRewardPoolPolygonLP.sol`
- All functions/constructors: `constructor`(L79), `deposit`(L147), `withdraw`(L163), `harvest`(L209), `chargeFees`(L229), `addLiquidity`(L263), `balanceOf`(L297), `balanceOfWant`(L307), `balanceOfPool`(L317), `retireStrat`(L327), `panic`(L347), `pause`(L357), `unpause`(L369), `_giveAllowances`(L385), `_removeAllowances`(L407)

### `deposit` (starts L147, showing L146–L192)
```solidity
 146: 
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
 160: 
 161: 
 162: 
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
```

### `withdraw` (starts L163, showing L162–L208)
```solidity
 162: 
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
 204: 
 205: 
 206: 
 207:     // compounds earnings and charges performance fee
 208: 
```

### `harvest` (starts L209, showing L208–L254)
```solidity
 208: 
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
 224: 
 225: 
 226: 
 227:     // performance fees
 228: 
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
```

### `retireStrat` (starts L327, showing L326–L372)
```solidity
 326: 
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
 342: 
 343: 
 344: 
 345:     // pauses deposits and withdraws all funds from third party systems.
 346: 
 347:     function panic() public onlyManager {
 348: 
 349:         pause();
 350: 
 351:         IRewardPool(rewardPool).withdraw(balanceOfPool());
 352: 
 353:     }
 354: 
 355: 
 356: 
 357:     function pause() public onlyManager {
 358: 
 359:         _pause();
 360: 
 361: 
 362: 
 363:         _removeAllowances();
 364: 
 365:     }
 366: 
 367: 
 368: 
 369:     function unpause() external onlyManager {
 370: 
 371:         _unpause();
 372: 
```

### `panic` (starts L347, showing L346–L392)
```solidity
 346: 
 347:     function panic() public onlyManager {
 348: 
 349:         pause();
 350: 
 351:         IRewardPool(rewardPool).withdraw(balanceOfPool());
 352: 
 353:     }
 354: 
 355: 
 356: 
 357:     function pause() public onlyManager {
 358: 
 359:         _pause();
 360: 
 361: 
 362: 
 363:         _removeAllowances();
 364: 
 365:     }
 366: 
 367: 
 368: 
 369:     function unpause() external onlyManager {
 370: 
 371:         _unpause();
 372: 
 373: 
 374: 
 375:         _giveAllowances();
 376: 
 377: 
 378: 
 379:         deposit();
 380: 
 381:     }
 382: 
 383: 
 384: 
 385:     function _giveAllowances() internal {
 386: 
 387:         IERC20(want).safeApprove(rewardPool, uint256(-1));
 388: 
 389:         IERC20(output).safeApprove(unirouter, uint256(-1));
 390: 
 391: 
 392: 
```

## `contracts/archive/vaults/BeefyVaultV6.sol`
- All functions/constructors: `constructor`(L47), `want`(L60), `balance`(L69), `available`(L79), `getPricePerFullShare`(L87), `depositAll`(L94), `deposit`(L102), `earn`(L123), `withdrawAll`(L132), `withdraw`(L141), `proposeStrat`(L163), `upgradeStrat`(L179), `inCaseTokensGetStuck`(L197)

### `deposit` (starts L102, showing L101–L147)
```solidity
 101:      */
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
 118: 
 119:     /**
 120:      * @dev Function to send funds into the strategy and put them to work. It's primarily called
 121:      * by the vault's deposit() function.
 122:      */
 123:     function earn() public {
 124:         uint _bal = available();
 125:         want().safeTransfer(address(strategy), _bal);
 126:         strategy.deposit();
 127:     }
 128: 
 129:     /**
 130:      * @dev A helper function to call withdraw() with all the sender's funds.
 131:      */
 132:     function withdrawAll() external {
 133:         withdraw(balanceOf(msg.sender));
 134:     }
 135: 
 136:     /**
 137:      * @dev Function to exit the system. The vault will withdraw the required tokens
 138:      * from the strategy and pay up the token holder. A proportional number of IOU
 139:      * tokens are burned in the process.
 140:      */
 141:     function withdraw(uint256 _shares) public {
 142:         uint256 r = (balance().mul(_shares)).div(totalSupply());
 143:         _burn(msg.sender, _shares);
 144: 
 145:         uint b = want().balanceOf(address(this));
 146:         if (b < r) {
 147:             uint _withdraw = r.sub(b);
```

### `earn` (starts L123, showing L122–L168)
```solidity
 122:      */
 123:     function earn() public {
 124:         uint _bal = available();
 125:         want().safeTransfer(address(strategy), _bal);
 126:         strategy.deposit();
 127:     }
 128: 
 129:     /**
 130:      * @dev A helper function to call withdraw() with all the sender's funds.
 131:      */
 132:     function withdrawAll() external {
 133:         withdraw(balanceOf(msg.sender));
 134:     }
 135: 
 136:     /**
 137:      * @dev Function to exit the system. The vault will withdraw the required tokens
 138:      * from the strategy and pay up the token holder. A proportional number of IOU
 139:      * tokens are burned in the process.
 140:      */
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
 158: 
 159:     /** 
 160:      * @dev Sets the candidate for the new strat to use with this vault.
 161:      * @param _implementation The address of the candidate strategy.  
 162:      */
 163:     function proposeStrat(address _implementation) public onlyOwner {
 164:         require(address(this) == IStrategy(_implementation).vault(), "Proposal not valid for this Vault");
 165:         stratCandidate = StratCandidate({
 166:             implementation: _implementation,
 167:             proposedTime: block.timestamp
 168:          });
```

### `withdrawAll` (starts L132, showing L131–L177)
```solidity
 131:      */
 132:     function withdrawAll() external {
 133:         withdraw(balanceOf(msg.sender));
 134:     }
 135: 
 136:     /**
 137:      * @dev Function to exit the system. The vault will withdraw the required tokens
 138:      * from the strategy and pay up the token holder. A proportional number of IOU
 139:      * tokens are burned in the process.
 140:      */
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
 158: 
 159:     /** 
 160:      * @dev Sets the candidate for the new strat to use with this vault.
 161:      * @param _implementation The address of the candidate strategy.  
 162:      */
 163:     function proposeStrat(address _implementation) public onlyOwner {
 164:         require(address(this) == IStrategy(_implementation).vault(), "Proposal not valid for this Vault");
 165:         stratCandidate = StratCandidate({
 166:             implementation: _implementation,
 167:             proposedTime: block.timestamp
 168:          });
 169: 
 170:         emit NewStratCandidate(_implementation);
 171:     }
 172: 
 173:     /** 
 174:      * @dev It switches the active strat for the strat candidate. After upgrading, the 
 175:      * candidate implementation is set to the 0x00 address, and proposedTime to a time 
 176:      * happening in +100 years for safety. 
 177:      */
```

### `withdraw` (starts L141, showing L140–L186)
```solidity
 140:      */
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
 158: 
 159:     /** 
 160:      * @dev Sets the candidate for the new strat to use with this vault.
 161:      * @param _implementation The address of the candidate strategy.  
 162:      */
 163:     function proposeStrat(address _implementation) public onlyOwner {
 164:         require(address(this) == IStrategy(_implementation).vault(), "Proposal not valid for this Vault");
 165:         stratCandidate = StratCandidate({
 166:             implementation: _implementation,
 167:             proposedTime: block.timestamp
 168:          });
 169: 
 170:         emit NewStratCandidate(_implementation);
 171:     }
 172: 
 173:     /** 
 174:      * @dev It switches the active strat for the strat candidate. After upgrading, the 
 175:      * candidate implementation is set to the 0x00 address, and proposedTime to a time 
 176:      * happening in +100 years for safety. 
 177:      */
 178: 
 179:     function upgradeStrat() public onlyOwner {
 180:         require(stratCandidate.implementation != address(0), "There is no candidate");
 181:         require(stratCandidate.proposedTime.add(approvalDelay) < block.timestamp, "Delay has not passed");
 182: 
 183:         emit UpgradeStrat(stratCandidate.implementation);
 184: 
 185:         strategy.retireStrat();
 186:         strategy = IStrategy(stratCandidate.implementation);
```

### `proposeStrat` (starts L163, showing L162–L203)
```solidity
 162:      */
 163:     function proposeStrat(address _implementation) public onlyOwner {
 164:         require(address(this) == IStrategy(_implementation).vault(), "Proposal not valid for this Vault");
 165:         stratCandidate = StratCandidate({
 166:             implementation: _implementation,
 167:             proposedTime: block.timestamp
 168:          });
 169: 
 170:         emit NewStratCandidate(_implementation);
 171:     }
 172: 
 173:     /** 
 174:      * @dev It switches the active strat for the strat candidate. After upgrading, the 
 175:      * candidate implementation is set to the 0x00 address, and proposedTime to a time 
 176:      * happening in +100 years for safety. 
 177:      */
 178: 
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
 192: 
 193:     /**
 194:      * @dev Rescues random funds stuck that the strat can't handle.
 195:      * @param _token address of the token to rescue.
 196:      */
 197:     function inCaseTokensGetStuck(address _token) external onlyOwner {
 198:         require(_token != address(want()), "!token");
 199: 
 200:         uint256 amount = IERC20(_token).balanceOf(address(this));
 201:         IERC20(_token).safeTransfer(msg.sender, amount);
 202:     }
 203: }
```

### `upgradeStrat` (starts L179, showing L178–L203)
```solidity
 178: 
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
 192: 
 193:     /**
 194:      * @dev Rescues random funds stuck that the strat can't handle.
 195:      * @param _token address of the token to rescue.
 196:      */
 197:     function inCaseTokensGetStuck(address _token) external onlyOwner {
 198:         require(_token != address(want()), "!token");
 199: 
 200:         uint256 amount = IERC20(_token).balanceOf(address(this));
 201:         IERC20(_token).safeTransfer(msg.sender, amount);
 202:     }
 203: }
```
