# 2026-11-24 — Deep Audit Slices (Entry Points & Sink Windows)

## `contracts/archive/infra/FlatBeefyZap.sol` (998 lines)
### Functions / Constructors
- L14: `name` — `function name() external pure returns (string memory);     function symbol() external pure returns (string memory);     function decimals() external pure return`
- L15: `symbol` — `function symbol() external pure returns (string memory);     function decimals() external pure returns (uint8);     function totalSupply() external view returns`
- L16: `decimals` — `function decimals() external pure returns (uint8);     function totalSupply() external view returns (uint);     function balanceOf(address owner) external view `
- L17: `totalSupply` — `function totalSupply() external view returns (uint);     function balanceOf(address owner) external view returns (uint);     function allowance(address owner, a`
- L18: `balanceOf` — `function balanceOf(address owner) external view returns (uint);     function allowance(address owner, address spender) external view returns (uint);      functi`
- L19: `allowance` — `function allowance(address owner, address spender) external view returns (uint);      function approve(address spender, uint value) external returns (bool);    `
- L21: `approve` — `function approve(address spender, uint value) external returns (bool);     function transfer(address to, uint value) external returns (bool);     function trans`
- L22: `transfer` — `function transfer(address to, uint value) external returns (bool);     function transferFrom(address from, address to, uint value) external returns (bool);     `
- L23: `transferFrom` — `function transferFrom(address from, address to, uint value) external returns (bool);      function DOMAIN_SEPARATOR() external view returns (bytes32);     funct`
- L25: `DOMAIN_SEPARATOR` — `function DOMAIN_SEPARATOR() external view returns (bytes32);     function PERMIT_TYPEHASH() external pure returns (bytes32);     function nonces(address owner) `
- L26: `PERMIT_TYPEHASH` — `function PERMIT_TYPEHASH() external pure returns (bytes32);     function nonces(address owner) external view returns (uint);      function permit(address owner,`
- L27: `nonces` — `function nonces(address owner) external view returns (uint);      function permit(address owner, address spender, uint value, uint deadline, uint8 v, bytes32 r,`
- L29: `permit` — `function permit(address owner, address spender, uint value, uint deadline, uint8 v, bytes32 r, bytes32 s) external;      event Mint(address indexed sender, uint`
- L43: `MINIMUM_LIQUIDITY` — `function MINIMUM_LIQUIDITY() external pure returns (uint);     function factory() external view returns (address);     function token0() external view returns (`
- L44: `factory` — `function factory() external view returns (address);     function token0() external view returns (address);     function token1() external view returns (address)`
- L45: `token0` — `function token0() external view returns (address);     function token1() external view returns (address);     function getReserves() external view returns (uint`
- L46: `token1` — `function token1() external view returns (address);     function getReserves() external view returns (uint112 reserve0, uint112 reserve1, uint32 blockTimestampLa`
- L47: `getReserves` — `function getReserves() external view returns (uint112 reserve0, uint112 reserve1, uint32 blockTimestampLast);     function price0CumulativeLast() external view `
- L48: `price0CumulativeLast` — `function price0CumulativeLast() external view returns (uint);     function price1CumulativeLast() external view returns (uint);     function kLast() external vi`
- L49: `price1CumulativeLast` — `function price1CumulativeLast() external view returns (uint);     function kLast() external view returns (uint);      function mint(address to) external returns`
- L50: `kLast` — `function kLast() external view returns (uint);      function mint(address to) external returns (uint liquidity);     function burn(address to) external returns `
- L52: `mint` — `function mint(address to) external returns (uint liquidity);     function burn(address to) external returns (uint amount0, uint amount1);     function swap(uint`
- L53: `burn` — `function burn(address to) external returns (uint amount0, uint amount1);     function swap(uint amount0Out, uint amount1Out, address to, bytes calldata data) ex`
- L54: `swap` — `function swap(uint amount0Out, uint amount1Out, address to, bytes calldata data) external;     function skim(address to) external;     function sync() external;`
- L55: `skim` — `function skim(address to) external;     function sync() external;      function initialize(address, address) external; }`
- L56: `sync` — `function sync() external;      function initialize(address, address) external; }`
- L58: `initialize` — `function initialize(address, address) external; }  // File: contracts/BIFI/zap/Babylonian.sol`
- L71: `sqrt` — `function sqrt(uint256 x) internal pure returns (uint256) {         if (x == 0) return 0;         // this block is equivalent to r = uint256(1) << (BitMath.mostS`
- L128: `totalSupply` — `function totalSupply() external view returns (uint256);      /**      * @dev Returns the amount of tokens owned by `account`.      */`
- L133: `balanceOf` — `function balanceOf(address account) external view returns (uint256);      /**      * @dev Moves `amount` tokens from the caller's account to `recipient`.      *`
- L142: `transfer` — `function transfer(address recipient, uint256 amount) external returns (bool);      /**      * @dev Returns the remaining number of tokens that `spender` will be`
- L151: `allowance` — `function allowance(address owner, address spender) external view returns (uint256);      /**      * @dev Sets `amount` as the allowance of `spender` over the ca`
- L167: `approve` — `function approve(address spender, uint256 amount) external returns (bool);      /**      * @dev Moves `amount` tokens from `sender` to `recipient` using the    `
- L178: `transferFrom` — `function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);      /**      * @dev Emitted when `value` tokens are moved fro`
- L224: `add` — `function add(uint256 a, uint256 b) internal pure returns (uint256) {         uint256 c = a + b;         require(c >= a, "SafeMath: addition overflow");         `
- L241: `sub` — `function sub(uint256 a, uint256 b) internal pure returns (uint256) {         return sub(a, b, "SafeMath: subtraction overflow");     }      /**`
- L255: `sub` — `function sub(uint256 a, uint256 b, string memory errorMessage) internal pure returns (uint256) {         require(b <= a, errorMessage);         uint256 c = a - `
- L272: `mul` — `function mul(uint256 a, uint256 b) internal pure returns (uint256) {         // Gas optimization: this is cheaper than requiring 'a' not being zero, but the    `
- L298: `div` — `function div(uint256 a, uint256 b) internal pure returns (uint256) {         return div(a, b, "SafeMath: division by zero");     }      /**`
- L314: `div` — `function div(uint256 a, uint256 b, string memory errorMessage) internal pure returns (uint256) {         require(b > 0, errorMessage);         uint256 c = a / b`
- L334: `mod` — `function mod(uint256 a, uint256 b) internal pure returns (uint256) {         return mod(a, b, "SafeMath: modulo by zero");     }      /**`
- L350: `mod` — `function mod(uint256 a, uint256 b, string memory errorMessage) internal pure returns (uint256) {         require(b != 0, errorMessage);         return a % b;   `
- L382: `isContract` — `function isContract(address account) internal view returns (bool) {         // This method relies on extcodesize, which returns 0 for contracts in         // co`
- L409: `sendValue` — `function sendValue(address payable recipient, uint256 amount) internal {         require(address(this).balance >= amount, "Address: insufficient balance");     `
- L435: `functionCall` — `function functionCall(address target, bytes memory data) internal returns (bytes memory) {       return functionCall(target, data, "Address: low-level call fail`
- L445: `functionCall` — `function functionCall(address target, bytes memory data, string memory errorMessage) internal returns (bytes memory) {         return functionCallWithValue(targ`
- L460: `functionCallWithValue` — `function functionCallWithValue(address target, bytes memory data, uint256 value) internal returns (bytes memory) {         return functionCallWithValue(target, `
- L470: `functionCallWithValue` — `function functionCallWithValue(address target, bytes memory data, uint256 value, string memory errorMessage) internal returns (bytes memory) {         require(a`
- L485: `functionStaticCall` — `function functionStaticCall(address target, bytes memory data) internal view returns (bytes memory) {         return functionStaticCall(target, data, "Address: `
- L495: `functionStaticCall` — `function functionStaticCall(address target, bytes memory data, string memory errorMessage) internal view returns (bytes memory) {         require(isContract(tar`
- L503: `_verifyCallResult` — `function _verifyCallResult(bool success, bytes memory returndata, string memory errorMessage) private pure returns(bytes memory) {         if (success) {       `
- L543: `safeTransfer` — `function safeTransfer(IERC20 token, address to, uint256 value) internal {         _callOptionalReturn(token, abi.encodeWithSelector(token.transfer.selector, to,`
- L547: `safeTransferFrom` — `function safeTransferFrom(IERC20 token, address from, address to, uint256 value) internal {         _callOptionalReturn(token, abi.encodeWithSelector(token.tran`
- L558: `safeApprove` — `function safeApprove(IERC20 token, address spender, uint256 value) internal {         // safeApprove should only be called when setting an initial allowance,   `
- L569: `safeIncreaseAllowance` — `function safeIncreaseAllowance(IERC20 token, address spender, uint256 value) internal {         uint256 newAllowance = token.allowance(address(this), spender).a`
- L574: `safeDecreaseAllowance` — `function safeDecreaseAllowance(IERC20 token, address spender, uint256 value) internal {         uint256 newAllowance = token.allowance(address(this), spender).s`
- L585: `_callOptionalReturn` — `function _callOptionalReturn(IERC20 token, bytes memory data) private {         // We need to perform a low level call here, to bypass Solidity's return data si`
- L609: `add` — `function add(uint256 x, uint256 y) internal pure returns (uint256 z) {         require((z = x + y) >= x);     }      /// @notice Returns x - y, reverts if under`
- L617: `sub` — `function sub(uint256 x, uint256 y) internal pure returns (uint256 z) {         require((z = x - y) <= x);     }      /// @notice Returns x * y, reverts if overf`
- L625: `mul` — `function mul(uint256 x, uint256 y) internal pure returns (uint256 z) {         require(x == 0 || (z = x * y) / x == y);     }      /// @notice Returns x + y, re`
- L633: `add` — `function add(int256 x, int256 y) internal pure returns (int256 z) {         require((z = x + y) >= x == (y >= 0));     }      /// @notice Returns x - y, reverts`
- L641: `sub` — `function sub(int256 x, int256 y) internal pure returns (int256 z) {         require((z = x - y) <= x == (y >= 0));     } }`
- L651: `factory` — `function factory() external pure returns (address);     function WETH() external pure returns (address);      function addLiquidity(         address tokenA,`
- L652: `WETH` — `function WETH() external pure returns (address);      function addLiquidity(         address tokenA,         address tokenB,`
- L654: `addLiquidity` — `function addLiquidity(         address tokenA,         address tokenB,         uint amountADesired,         uint amountBDesired,`
- L664: `addLiquidityETH` — `function addLiquidityETH(         address token,         uint amountTokenDesired,         uint amountTokenMin,         uint amountETHMin,`
- L672: `removeLiquidity` — `function removeLiquidity(         address tokenA,         address tokenB,         uint liquidity,         uint amountAMin,`
- L681: `removeLiquidityETH` — `function removeLiquidityETH(         address token,         uint liquidity,         uint amountTokenMin,         uint amountETHMin,`
- L689: `removeLiquidityWithPermit` — `function removeLiquidityWithPermit(         address tokenA,         address tokenB,         uint liquidity,         uint amountAMin,`
- L699: `removeLiquidityETHWithPermit` — `function removeLiquidityETHWithPermit(         address token,         uint liquidity,         uint amountTokenMin,         uint amountETHMin,`
- L708: `swapExactTokensForTokens` — `function swapExactTokensForTokens(         uint amountIn,         uint amountOutMin,         address[] calldata path,         address to,`
- L715: `swapTokensForExactTokens` — `function swapTokensForExactTokens(         uint amountOut,         uint amountInMax,         address[] calldata path,         address to,`
- L722: `swapExactETHForTokens` — `function swapExactETHForTokens(uint amountOutMin, address[] calldata path, address to, uint deadline)         external         payable         returns (uint[] m`
- L726: `swapTokensForExactETH` — `function swapTokensForExactETH(uint amountOut, uint amountInMax, address[] calldata path, address to, uint deadline)         external         returns (uint[] me`
- L729: `swapExactTokensForETH` — `function swapExactTokensForETH(uint amountIn, uint amountOutMin, address[] calldata path, address to, uint deadline)         external         returns (uint[] me`
- L732: `swapETHForExactTokens` — `function swapETHForExactTokens(uint amountOut, address[] calldata path, address to, uint deadline)         external         payable         returns (uint[] memo`
- L737: `quote` — `function quote(uint amountA, uint reserveA, uint reserveB) external pure returns (uint amountB);     function getAmountOut(uint amountIn, uint reserveIn, uint r`
- L738: `getAmountOut` — `function getAmountOut(uint amountIn, uint reserveIn, uint reserveOut) external pure returns (uint amountOut);     function getAmountIn(uint amountOut, uint rese`
- L739: `getAmountIn` — `function getAmountIn(uint amountOut, uint reserveIn, uint reserveOut) external pure returns (uint amountIn);     function getAmountsOut(uint amountIn, address[]`
- L740: `getAmountsOut` — `function getAmountsOut(uint amountIn, address[] calldata path) external view returns (uint[] memory amounts);     function getAmountsIn(uint amountOut, address[`
- L741: `getAmountsIn` — `function getAmountsIn(uint amountOut, address[] calldata path) external view returns (uint[] memory amounts); }  // File: contracts/BIFI/zap/IUniswapV2Router02.`
- L750: `removeLiquidityETHSupportingFeeOnTransferTokens` — `function removeLiquidityETHSupportingFeeOnTransferTokens(         address token,         uint liquidity,         uint amountTokenMin,         uint amountETHMin,`
- L758: `removeLiquidityETHWithPermitSupportingFeeOnTransferTokens` — `function removeLiquidityETHWithPermitSupportingFeeOnTransferTokens(         address token,         uint liquidity,         uint amountTokenMin,         uint amo`
- L768: `swapExactTokensForTokensSupportingFeeOnTransferTokens` — `function swapExactTokensForTokensSupportingFeeOnTransferTokens(         uint amountIn,         uint amountOutMin,         address[] calldata path,         addre`
- L775: `swapExactETHForTokensSupportingFeeOnTransferTokens` — `function swapExactETHForTokensSupportingFeeOnTransferTokens(         uint amountOutMin,         address[] calldata path,         address to,         uint deadli`
- L781: `swapExactTokensForETHSupportingFeeOnTransferTokens` — `function swapExactTokensForETHSupportingFeeOnTransferTokens(         uint amountIn,         uint amountOutMin,         address[] calldata path,         address `
- L814: `deposit` — `function deposit() external payable;     function withdraw(uint256 wad) external; }  interface IBeefyVaultV6 is IERC20 {`
- L815: `withdraw` — `function withdraw(uint256 wad) external; }  interface IBeefyVaultV6 is IERC20 {     function deposit(uint256 amount) external;`
- L819: `deposit` — `function deposit(uint256 amount) external;     function withdraw(uint256 shares) external;     function want() external pure returns (address); }`
- L820: `withdraw` — `function withdraw(uint256 shares) external;     function want() external pure returns (address); }  contract BeefyUniV2Zap {`
- L821: `want` — `function want() external pure returns (address); }  contract BeefyUniV2Zap {     using LowGasSafeMath for uint256;`
- L833: `constructor` — `constructor(address _router, address _WETH) {         router = IUniswapV2Router02(_router);         WETH = _WETH;     }`
- L842: `beefInETH` — `function beefInETH (address beefyVault, uint256 tokenAmountOutMin) external payable {         require(msg.value >= minimumAmount, 'Beefy: Insignificant input am`
- L850: `beefIn` — `function beefIn (address beefyVault, uint256 tokenAmountOutMin, address tokenIn, uint256 tokenInAmount) external {         require(tokenInAmount >= minimumAmoun`
- L859: `beefOut` — `function beefOut (address beefyVault, uint256 withdrawAmount) external {         (IBeefyVaultV6 vault, IUniswapV2Pair pair) = _getVaultPair(beefyVault);        `
- L878: `beefOutAndSwap` — `function beefOutAndSwap(address beefyVault, uint256 withdrawAmount, address desiredToken, uint256 desiredTokenOutMin) external {         (IBeefyVaultV6 vault, I`
- L899: `_removeLiqudity` — `function _removeLiqudity(address pair, address to) private {         IERC20(pair).safeTransfer(pair, IERC20(pair).balanceOf(address(this)));         (uint256 am`
- L907: `_getVaultPair` — `function _getVaultPair (address beefyVault) private view returns (IBeefyVaultV6 vault, IUniswapV2Pair pair) {         vault = IBeefyVaultV6(beefyVault);        `
- L913: `_swapAndStake` — `function _swapAndStake(address beefyVault, uint256 tokenAmountOutMin, address tokenIn) private {         (IBeefyVaultV6 vault, IUniswapV2Pair pair) = _getVaultP`
- L949: `_returnAssets` — `function _returnAssets(address[] memory tokens) private {         uint256 balance;         for (uint256 i; i < tokens.length; i++) {             balance = IERC2`
- L965: `_getSwapAmount` — `function _getSwapAmount(uint256 investmentA, uint256 reserveA, uint256 reserveB) private view returns (uint256 swapAmount) {         uint256 halfInvestment = in`
- L972: `estimateSwap` — `function estimateSwap(address beefyVault, address tokenIn, uint256 fullInvestmentIn) public view returns(uint256 swapAmountIn, uint256 swapAmountOut, address sw`
- L987: `checkWETH` — `function checkWETH() public view returns (bool isValid) {         isValid = WETH == router.WETH();         require(isValid, 'Beefy: WETH address not matching Ro`
- L992: `_approveTokenIfNeeded` — `function _approveTokenIfNeeded(address token, address spender) private {         if (IERC20(token).allowance(address(this), spender) == 0) {             IERC20(`

### Sink Windows (±8 lines)
#### Line 18 (L10–L26)
```solidity
     10: interface IUniswapV2Pair {
     11:     event Approval(address indexed owner, address indexed spender, uint value);
     12:     event Transfer(address indexed from, address indexed to, uint value);
     13: 
     14:     function name() external pure returns (string memory);
     15:     function symbol() external pure returns (string memory);
     16:     function decimals() external pure returns (uint8);
     17:     function totalSupply() external view returns (uint);
>>   18:     function balanceOf(address owner) external view returns (uint);
     19:     function allowance(address owner, address spender) external view returns (uint);
     20: 
     21:     function approve(address spender, uint value) external returns (bool);
     22:     function transfer(address to, uint value) external returns (bool);
     23:     function transferFrom(address from, address to, uint value) external returns (bool);
     24: 
     25:     function DOMAIN_SEPARATOR() external view returns (bytes32);
     26:     function PERMIT_TYPEHASH() external pure returns (bytes32);
```

#### Line 21 (L13–L29)
```solidity
     13: 
     14:     function name() external pure returns (string memory);
     15:     function symbol() external pure returns (string memory);
     16:     function decimals() external pure returns (uint8);
     17:     function totalSupply() external view returns (uint);
     18:     function balanceOf(address owner) external view returns (uint);
     19:     function allowance(address owner, address spender) external view returns (uint);
     20: 
>>   21:     function approve(address spender, uint value) external returns (bool);
     22:     function transfer(address to, uint value) external returns (bool);
     23:     function transferFrom(address from, address to, uint value) external returns (bool);
     24: 
     25:     function DOMAIN_SEPARATOR() external view returns (bytes32);
     26:     function PERMIT_TYPEHASH() external pure returns (bytes32);
     27:     function nonces(address owner) external view returns (uint);
     28: 
     29:     function permit(address owner, address spender, uint value, uint deadline, uint8 v, bytes32 r, bytes32 s) external;
```

#### Line 47 (L39–L55)
```solidity
     39:         address indexed to
     40:     );
     41:     event Sync(uint112 reserve0, uint112 reserve1);
     42: 
     43:     function MINIMUM_LIQUIDITY() external pure returns (uint);
     44:     function factory() external view returns (address);
     45:     function token0() external view returns (address);
     46:     function token1() external view returns (address);
>>   47:     function getReserves() external view returns (uint112 reserve0, uint112 reserve1, uint32 blockTimestampLast);
     48:     function price0CumulativeLast() external view returns (uint);
     49:     function price1CumulativeLast() external view returns (uint);
     50:     function kLast() external view returns (uint);
     51: 
     52:     function mint(address to) external returns (uint liquidity);
     53:     function burn(address to) external returns (uint amount0, uint amount1);
     54:     function swap(uint amount0Out, uint amount1Out, address to, bytes calldata data) external;
     55:     function skim(address to) external;
```

#### Line 133 (L125–L141)
```solidity
    125:     /**
    126:      * @dev Returns the amount of tokens in existence.
    127:      */
    128:     function totalSupply() external view returns (uint256);
    129: 
    130:     /**
    131:      * @dev Returns the amount of tokens owned by `account`.
    132:      */
>>  133:     function balanceOf(address account) external view returns (uint256);
    134: 
    135:     /**
    136:      * @dev Moves `amount` tokens from the caller's account to `recipient`.
    137:      *
    138:      * Returns a boolean value indicating whether the operation succeeded.
    139:      *
    140:      * Emits a {Transfer} event.
    141:      */
```

#### Line 149 (L141–L157)
```solidity
    141:      */
    142:     function transfer(address recipient, uint256 amount) external returns (bool);
    143: 
    144:     /**
    145:      * @dev Returns the remaining number of tokens that `spender` will be
    146:      * allowed to spend on behalf of `owner` through {transferFrom}. This is
    147:      * zero by default.
    148:      *
>>  149:      * This value changes when {approve} or {transferFrom} are called.
    150:      */
    151:     function allowance(address owner, address spender) external view returns (uint256);
    152: 
    153:     /**
    154:      * @dev Sets `amount` as the allowance of `spender` over the caller's tokens.
    155:      *
    156:      * Returns a boolean value indicating whether the operation succeeded.
    157:      *
```

#### Line 167 (L159–L175)
```solidity
    159:      * that someone may use both the old and the new allowance by unfortunate
    160:      * transaction ordering. One possible solution to mitigate this race
    161:      * condition is to first reduce the spender's allowance to 0 and set the
    162:      * desired value afterwards:
    163:      * https://github.com/ethereum/EIPs/issues/20#issuecomment-263524729
    164:      *
    165:      * Emits an {Approval} event.
    166:      */
>>  167:     function approve(address spender, uint256 amount) external returns (bool);
    168: 
    169:     /**
    170:      * @dev Moves `amount` tokens from `sender` to `recipient` using the
    171:      * allowance mechanism. `amount` is then deducted from the caller's
    172:      * allowance.
    173:      *
    174:      * Returns a boolean value indicating whether the operation succeeded.
    175:      *
```

#### Line 190 (L182–L198)
```solidity
    182:      * another (`to`).
    183:      *
    184:      * Note that `value` may be zero.
    185:      */
    186:     event Transfer(address indexed from, address indexed to, uint256 value);
    187: 
    188:     /**
    189:      * @dev Emitted when the allowance of a `spender` for an `owner` is set by
>>  190:      * a call to {approve}. `value` is the new allowance.
    191:      */
    192:     event Approval(address indexed owner, address indexed spender, uint256 value);
    193: }
    194: 
    195: // File: contracts/BIFI/zap/SafeMath.sol
    196: 
    197: 
    198: pragma solidity ^0.8.0;
```

#### Line 537 (L529–L545)
```solidity
    529: 
    530: /**
    531:  * @title SafeERC20
    532:  * @dev Wrappers around ERC20 operations that throw on failure (when the token
    533:  * contract returns false). Tokens that return no value (and instead revert or
    534:  * throw on failure) are also supported, non-reverting calls are assumed to be
    535:  * successful.
    536:  * To use this library you can add a `using SafeERC20 for IERC20;` statement to your contract,
>>  537:  * which allows you to call the safe operations as `token.safeTransfer(...)`, etc.
    538:  */
    539: library SafeERC20 {
    540:     using SafeMath for uint256;
    541:     using Address for address;
    542: 
    543:     function safeTransfer(IERC20 token, address to, uint256 value) internal {
    544:         _callOptionalReturn(token, abi.encodeWithSelector(token.transfer.selector, to, value));
    545:     }
```

#### Line 543 (L535–L551)
```solidity
    535:  * successful.
    536:  * To use this library you can add a `using SafeERC20 for IERC20;` statement to your contract,
    537:  * which allows you to call the safe operations as `token.safeTransfer(...)`, etc.
    538:  */
    539: library SafeERC20 {
    540:     using SafeMath for uint256;
    541:     using Address for address;
    542: 
>>  543:     function safeTransfer(IERC20 token, address to, uint256 value) internal {
    544:         _callOptionalReturn(token, abi.encodeWithSelector(token.transfer.selector, to, value));
    545:     }
    546: 
    547:     function safeTransferFrom(IERC20 token, address from, address to, uint256 value) internal {
    548:         _callOptionalReturn(token, abi.encodeWithSelector(token.transferFrom.selector, from, to, value));
    549:     }
    550: 
    551:     /**
```

#### Line 547 (L539–L555)
```solidity
    539: library SafeERC20 {
    540:     using SafeMath for uint256;
    541:     using Address for address;
    542: 
    543:     function safeTransfer(IERC20 token, address to, uint256 value) internal {
    544:         _callOptionalReturn(token, abi.encodeWithSelector(token.transfer.selector, to, value));
    545:     }
    546: 
>>  547:     function safeTransferFrom(IERC20 token, address from, address to, uint256 value) internal {
    548:         _callOptionalReturn(token, abi.encodeWithSelector(token.transferFrom.selector, from, to, value));
    549:     }
    550: 
    551:     /**
    552:      * @dev Deprecated. This function has issues similar to the ones found in
    553:      * {IERC20-approve}, and its usage is discouraged.
    554:      *
    555:      * Whenever possible, use {safeIncreaseAllowance} and
```

#### Line 553 (L545–L561)
```solidity
    545:     }
    546: 
    547:     function safeTransferFrom(IERC20 token, address from, address to, uint256 value) internal {
    548:         _callOptionalReturn(token, abi.encodeWithSelector(token.transferFrom.selector, from, to, value));
    549:     }
    550: 
    551:     /**
    552:      * @dev Deprecated. This function has issues similar to the ones found in
>>  553:      * {IERC20-approve}, and its usage is discouraged.
    554:      *
    555:      * Whenever possible, use {safeIncreaseAllowance} and
    556:      * {safeDecreaseAllowance} instead.
    557:      */
    558:     function safeApprove(IERC20 token, address spender, uint256 value) internal {
    559:         // safeApprove should only be called when setting an initial allowance,
    560:         // or when resetting it to zero. To increase and decrease it, use
    561:         // 'safeIncreaseAllowance' and 'safeDecreaseAllowance'
```

#### Line 558 (L550–L566)
```solidity
    550: 
    551:     /**
    552:      * @dev Deprecated. This function has issues similar to the ones found in
    553:      * {IERC20-approve}, and its usage is discouraged.
    554:      *
    555:      * Whenever possible, use {safeIncreaseAllowance} and
    556:      * {safeDecreaseAllowance} instead.
    557:      */
>>  558:     function safeApprove(IERC20 token, address spender, uint256 value) internal {
    559:         // safeApprove should only be called when setting an initial allowance,
    560:         // or when resetting it to zero. To increase and decrease it, use
    561:         // 'safeIncreaseAllowance' and 'safeDecreaseAllowance'
    562:         // solhint-disable-next-line max-line-length
    563:         require((value == 0) || (token.allowance(address(this), spender) == 0),
    564:             "SafeERC20: approve from non-zero to non-zero allowance"
    565:         );
    566:         _callOptionalReturn(token, abi.encodeWithSelector(token.approve.selector, spender, value));
```

#### Line 559 (L551–L567)
```solidity
    551:     /**
    552:      * @dev Deprecated. This function has issues similar to the ones found in
    553:      * {IERC20-approve}, and its usage is discouraged.
    554:      *
    555:      * Whenever possible, use {safeIncreaseAllowance} and
    556:      * {safeDecreaseAllowance} instead.
    557:      */
    558:     function safeApprove(IERC20 token, address spender, uint256 value) internal {
>>  559:         // safeApprove should only be called when setting an initial allowance,
    560:         // or when resetting it to zero. To increase and decrease it, use
    561:         // 'safeIncreaseAllowance' and 'safeDecreaseAllowance'
    562:         // solhint-disable-next-line max-line-length
    563:         require((value == 0) || (token.allowance(address(this), spender) == 0),
    564:             "SafeERC20: approve from non-zero to non-zero allowance"
    565:         );
    566:         _callOptionalReturn(token, abi.encodeWithSelector(token.approve.selector, spender, value));
    567:     }
```

#### Line 564 (L556–L572)
```solidity
    556:      * {safeDecreaseAllowance} instead.
    557:      */
    558:     function safeApprove(IERC20 token, address spender, uint256 value) internal {
    559:         // safeApprove should only be called when setting an initial allowance,
    560:         // or when resetting it to zero. To increase and decrease it, use
    561:         // 'safeIncreaseAllowance' and 'safeDecreaseAllowance'
    562:         // solhint-disable-next-line max-line-length
    563:         require((value == 0) || (token.allowance(address(this), spender) == 0),
>>  564:             "SafeERC20: approve from non-zero to non-zero allowance"
    565:         );
    566:         _callOptionalReturn(token, abi.encodeWithSelector(token.approve.selector, spender, value));
    567:     }
    568: 
    569:     function safeIncreaseAllowance(IERC20 token, address spender, uint256 value) internal {
    570:         uint256 newAllowance = token.allowance(address(this), spender).add(value);
    571:         _callOptionalReturn(token, abi.encodeWithSelector(token.approve.selector, spender, newAllowance));
    572:     }
```

#### Line 566 (L558–L574)
```solidity
    558:     function safeApprove(IERC20 token, address spender, uint256 value) internal {
    559:         // safeApprove should only be called when setting an initial allowance,
    560:         // or when resetting it to zero. To increase and decrease it, use
    561:         // 'safeIncreaseAllowance' and 'safeDecreaseAllowance'
    562:         // solhint-disable-next-line max-line-length
    563:         require((value == 0) || (token.allowance(address(this), spender) == 0),
    564:             "SafeERC20: approve from non-zero to non-zero allowance"
    565:         );
>>  566:         _callOptionalReturn(token, abi.encodeWithSelector(token.approve.selector, spender, value));
    567:     }
    568: 
    569:     function safeIncreaseAllowance(IERC20 token, address spender, uint256 value) internal {
    570:         uint256 newAllowance = token.allowance(address(this), spender).add(value);
    571:         _callOptionalReturn(token, abi.encodeWithSelector(token.approve.selector, spender, newAllowance));
    572:     }
    573: 
    574:     function safeDecreaseAllowance(IERC20 token, address spender, uint256 value) internal {
```

#### Line 571 (L563–L579)
```solidity
    563:         require((value == 0) || (token.allowance(address(this), spender) == 0),
    564:             "SafeERC20: approve from non-zero to non-zero allowance"
    565:         );
    566:         _callOptionalReturn(token, abi.encodeWithSelector(token.approve.selector, spender, value));
    567:     }
    568: 
    569:     function safeIncreaseAllowance(IERC20 token, address spender, uint256 value) internal {
    570:         uint256 newAllowance = token.allowance(address(this), spender).add(value);
>>  571:         _callOptionalReturn(token, abi.encodeWithSelector(token.approve.selector, spender, newAllowance));
    572:     }
    573: 
    574:     function safeDecreaseAllowance(IERC20 token, address spender, uint256 value) internal {
    575:         uint256 newAllowance = token.allowance(address(this), spender).sub(value, "SafeERC20: decreased allowance below zero");
    576:         _callOptionalReturn(token, abi.encodeWithSelector(token.approve.selector, spender, newAllowance));
    577:     }
    578: 
    579:     /**
```

#### Line 576 (L568–L584)
```solidity
    568: 
    569:     function safeIncreaseAllowance(IERC20 token, address spender, uint256 value) internal {
    570:         uint256 newAllowance = token.allowance(address(this), spender).add(value);
    571:         _callOptionalReturn(token, abi.encodeWithSelector(token.approve.selector, spender, newAllowance));
    572:     }
    573: 
    574:     function safeDecreaseAllowance(IERC20 token, address spender, uint256 value) internal {
    575:         uint256 newAllowance = token.allowance(address(this), spender).sub(value, "SafeERC20: decreased allowance below zero");
>>  576:         _callOptionalReturn(token, abi.encodeWithSelector(token.approve.selector, spender, newAllowance));
    577:     }
    578: 
    579:     /**
    580:      * @dev Imitates a Solidity high-level call (i.e. a regular function call to a contract), relaxing the requirement
    581:      * on the return value: the return value is optional (but if data is returned, it must not be false).
    582:      * @param token The token targeted by the call.
    583:      * @param data The call data (encoded using abi.encode or one of its variants).
    584:      */
```

#### Line 654 (L646–L662)
```solidity
    646: // File: contracts/BIFI/zap/IUniswapV2Router01.sol
    647: 
    648: pragma solidity ^0.8.0;
    649: 
    650: interface IUniswapV2Router01 {
    651:     function factory() external pure returns (address);
    652:     function WETH() external pure returns (address);
    653: 
>>  654:     function addLiquidity(
    655:         address tokenA,
    656:         address tokenB,
    657:         uint amountADesired,
    658:         uint amountBDesired,
    659:         uint amountAMin,
    660:         uint amountBMin,
    661:         address to,
    662:         uint deadline
```

#### Line 664 (L656–L672)
```solidity
    656:         address tokenB,
    657:         uint amountADesired,
    658:         uint amountBDesired,
    659:         uint amountAMin,
    660:         uint amountBMin,
    661:         address to,
    662:         uint deadline
    663:     ) external returns (uint amountA, uint amountB, uint liquidity);
>>  664:     function addLiquidityETH(
    665:         address token,
    666:         uint amountTokenDesired,
    667:         uint amountTokenMin,
    668:         uint amountETHMin,
    669:         address to,
    670:         uint deadline
    671:     ) external payable returns (uint amountToken, uint amountETH, uint liquidity);
    672:     function removeLiquidity(
```

#### Line 672 (L664–L680)
```solidity
    664:     function addLiquidityETH(
    665:         address token,
    666:         uint amountTokenDesired,
    667:         uint amountTokenMin,
    668:         uint amountETHMin,
    669:         address to,
    670:         uint deadline
    671:     ) external payable returns (uint amountToken, uint amountETH, uint liquidity);
>>  672:     function removeLiquidity(
    673:         address tokenA,
    674:         address tokenB,
    675:         uint liquidity,
    676:         uint amountAMin,
    677:         uint amountBMin,
    678:         address to,
    679:         uint deadline
    680:     ) external returns (uint amountA, uint amountB);
```

#### Line 681 (L673–L689)
```solidity
    673:         address tokenA,
    674:         address tokenB,
    675:         uint liquidity,
    676:         uint amountAMin,
    677:         uint amountBMin,
    678:         address to,
    679:         uint deadline
    680:     ) external returns (uint amountA, uint amountB);
>>  681:     function removeLiquidityETH(
    682:         address token,
    683:         uint liquidity,
    684:         uint amountTokenMin,
    685:         uint amountETHMin,
    686:         address to,
    687:         uint deadline
    688:     ) external returns (uint amountToken, uint amountETH);
    689:     function removeLiquidityWithPermit(
```

#### Line 689 (L681–L697)
```solidity
    681:     function removeLiquidityETH(
    682:         address token,
    683:         uint liquidity,
    684:         uint amountTokenMin,
    685:         uint amountETHMin,
    686:         address to,
    687:         uint deadline
    688:     ) external returns (uint amountToken, uint amountETH);
>>  689:     function removeLiquidityWithPermit(
    690:         address tokenA,
    691:         address tokenB,
    692:         uint liquidity,
    693:         uint amountAMin,
    694:         uint amountBMin,
    695:         address to,
    696:         uint deadline,
    697:         bool approveMax, uint8 v, bytes32 r, bytes32 s
```

#### Line 699 (L691–L707)
```solidity
    691:         address tokenB,
    692:         uint liquidity,
    693:         uint amountAMin,
    694:         uint amountBMin,
    695:         address to,
    696:         uint deadline,
    697:         bool approveMax, uint8 v, bytes32 r, bytes32 s
    698:     ) external returns (uint amountA, uint amountB);
>>  699:     function removeLiquidityETHWithPermit(
    700:         address token,
    701:         uint liquidity,
    702:         uint amountTokenMin,
    703:         uint amountETHMin,
    704:         address to,
    705:         uint deadline,
    706:         bool approveMax, uint8 v, bytes32 r, bytes32 s
    707:     ) external returns (uint amountToken, uint amountETH);
```

#### Line 708 (L700–L716)
```solidity
    700:         address token,
    701:         uint liquidity,
    702:         uint amountTokenMin,
    703:         uint amountETHMin,
    704:         address to,
    705:         uint deadline,
    706:         bool approveMax, uint8 v, bytes32 r, bytes32 s
    707:     ) external returns (uint amountToken, uint amountETH);
>>  708:     function swapExactTokensForTokens(
    709:         uint amountIn,
    710:         uint amountOutMin,
    711:         address[] calldata path,
    712:         address to,
    713:         uint deadline
    714:     ) external returns (uint[] memory amounts);
    715:     function swapTokensForExactTokens(
    716:         uint amountOut,
```

#### Line 722 (L714–L730)
```solidity
    714:     ) external returns (uint[] memory amounts);
    715:     function swapTokensForExactTokens(
    716:         uint amountOut,
    717:         uint amountInMax,
    718:         address[] calldata path,
    719:         address to,
    720:         uint deadline
    721:     ) external returns (uint[] memory amounts);
>>  722:     function swapExactETHForTokens(uint amountOutMin, address[] calldata path, address to, uint deadline)
    723:         external
    724:         payable
    725:         returns (uint[] memory amounts);
    726:     function swapTokensForExactETH(uint amountOut, uint amountInMax, address[] calldata path, address to, uint deadline)
    727:         external
    728:         returns (uint[] memory amounts);
    729:     function swapExactTokensForETH(uint amountIn, uint amountOutMin, address[] calldata path, address to, uint deadline)
    730:         external
```

#### Line 729 (L721–L737)
```solidity
    721:     ) external returns (uint[] memory amounts);
    722:     function swapExactETHForTokens(uint amountOutMin, address[] calldata path, address to, uint deadline)
    723:         external
    724:         payable
    725:         returns (uint[] memory amounts);
    726:     function swapTokensForExactETH(uint amountOut, uint amountInMax, address[] calldata path, address to, uint deadline)
    727:         external
    728:         returns (uint[] memory amounts);
>>  729:     function swapExactTokensForETH(uint amountIn, uint amountOutMin, address[] calldata path, address to, uint deadline)
    730:         external
    731:         returns (uint[] memory amounts);
    732:     function swapETHForExactTokens(uint amountOut, address[] calldata path, address to, uint deadline)
    733:         external
    734:         payable
    735:         returns (uint[] memory amounts);
    736: 
    737:     function quote(uint amountA, uint reserveA, uint reserveB) external pure returns (uint amountB);
```

#### Line 750 (L742–L758)
```solidity
    742: }
    743: 
    744: // File: contracts/BIFI/zap/IUniswapV2Router02.sol
    745: 
    746: pragma solidity ^0.8.0;
    747: 
    748: 
    749: interface IUniswapV2Router02 is IUniswapV2Router01 {
>>  750:     function removeLiquidityETHSupportingFeeOnTransferTokens(
    751:         address token,
    752:         uint liquidity,
    753:         uint amountTokenMin,
    754:         uint amountETHMin,
    755:         address to,
    756:         uint deadline
    757:     ) external returns (uint amountETH);
    758:     function removeLiquidityETHWithPermitSupportingFeeOnTransferTokens(
```

#### Line 758 (L750–L766)
```solidity
    750:     function removeLiquidityETHSupportingFeeOnTransferTokens(
    751:         address token,
    752:         uint liquidity,
    753:         uint amountTokenMin,
    754:         uint amountETHMin,
    755:         address to,
    756:         uint deadline
    757:     ) external returns (uint amountETH);
>>  758:     function removeLiquidityETHWithPermitSupportingFeeOnTransferTokens(
    759:         address token,
    760:         uint liquidity,
    761:         uint amountTokenMin,
    762:         uint amountETHMin,
    763:         address to,
    764:         uint deadline,
    765:         bool approveMax, uint8 v, bytes32 r, bytes32 s
    766:     ) external returns (uint amountETH);
```

#### Line 768 (L760–L776)
```solidity
    760:         uint liquidity,
    761:         uint amountTokenMin,
    762:         uint amountETHMin,
    763:         address to,
    764:         uint deadline,
    765:         bool approveMax, uint8 v, bytes32 r, bytes32 s
    766:     ) external returns (uint amountETH);
    767: 
>>  768:     function swapExactTokensForTokensSupportingFeeOnTransferTokens(
    769:         uint amountIn,
    770:         uint amountOutMin,
    771:         address[] calldata path,
    772:         address to,
    773:         uint deadline
    774:     ) external;
    775:     function swapExactETHForTokensSupportingFeeOnTransferTokens(
    776:         uint amountOutMin,
```

#### Line 775 (L767–L783)
```solidity
    767: 
    768:     function swapExactTokensForTokensSupportingFeeOnTransferTokens(
    769:         uint amountIn,
    770:         uint amountOutMin,
    771:         address[] calldata path,
    772:         address to,
    773:         uint deadline
    774:     ) external;
>>  775:     function swapExactETHForTokensSupportingFeeOnTransferTokens(
    776:         uint amountOutMin,
    777:         address[] calldata path,
    778:         address to,
    779:         uint deadline
    780:     ) external payable;
    781:     function swapExactTokensForETHSupportingFeeOnTransferTokens(
    782:         uint amountIn,
    783:         uint amountOutMin,
```

#### Line 781 (L773–L789)
```solidity
    773:         uint deadline
    774:     ) external;
    775:     function swapExactETHForTokensSupportingFeeOnTransferTokens(
    776:         uint amountOutMin,
    777:         address[] calldata path,
    778:         address to,
    779:         uint deadline
    780:     ) external payable;
>>  781:     function swapExactTokensForETHSupportingFeeOnTransferTokens(
    782:         uint amountIn,
    783:         uint amountOutMin,
    784:         address[] calldata path,
    785:         address to,
    786:         uint deadline
    787:     ) external;
    788: }
    789: 
```

#### Line 854 (L846–L862)
```solidity
    846: 
    847:         _swapAndStake(beefyVault, tokenAmountOutMin, WETH);
    848:     }
    849: 
    850:     function beefIn (address beefyVault, uint256 tokenAmountOutMin, address tokenIn, uint256 tokenInAmount) external {
    851:         require(tokenInAmount >= minimumAmount, 'Beefy: Insignificant input amount');
    852:         require(IERC20(tokenIn).allowance(msg.sender, address(this)) >= tokenInAmount, 'Beefy: Input token is not approved');
    853: 
>>  854:         IERC20(tokenIn).safeTransferFrom(msg.sender, address(this), tokenInAmount);
    855: 
    856:         _swapAndStake(beefyVault, tokenAmountOutMin, tokenIn);
    857:     }
    858: 
    859:     function beefOut (address beefyVault, uint256 withdrawAmount) external {
    860:         (IBeefyVaultV6 vault, IUniswapV2Pair pair) = _getVaultPair(beefyVault);
    861: 
    862:         IERC20(beefyVault).safeTransferFrom(msg.sender, address(this), withdrawAmount);
```

#### Line 862 (L854–L870)
```solidity
    854:         IERC20(tokenIn).safeTransferFrom(msg.sender, address(this), tokenInAmount);
    855: 
    856:         _swapAndStake(beefyVault, tokenAmountOutMin, tokenIn);
    857:     }
    858: 
    859:     function beefOut (address beefyVault, uint256 withdrawAmount) external {
    860:         (IBeefyVaultV6 vault, IUniswapV2Pair pair) = _getVaultPair(beefyVault);
    861: 
>>  862:         IERC20(beefyVault).safeTransferFrom(msg.sender, address(this), withdrawAmount);
    863:         vault.withdraw(withdrawAmount);
    864: 
    865:         if (pair.token0() != WETH && pair.token1() != WETH) {
    866:             return _removeLiqudity(address(pair), msg.sender);
    867:         }
    868: 
    869:         _removeLiqudity(address(pair), address(this));
    870: 
```

#### Line 884 (L876–L892)
```solidity
    876:     }
    877: 
    878:     function beefOutAndSwap(address beefyVault, uint256 withdrawAmount, address desiredToken, uint256 desiredTokenOutMin) external {
    879:         (IBeefyVaultV6 vault, IUniswapV2Pair pair) = _getVaultPair(beefyVault);
    880:         address token0 = pair.token0();
    881:         address token1 = pair.token1();
    882:         require(token0 == desiredToken || token1 == desiredToken, 'Beefy: desired token not present in liqudity pair');
    883: 
>>  884:         vault.safeTransferFrom(msg.sender, address(this), withdrawAmount);
    885:         vault.withdraw(withdrawAmount);
    886:         _removeLiqudity(address(pair), address(this));
    887: 
    888:         address swapToken = token1 == desiredToken ? token0 : token1;
    889:         address[] memory path = new address[](2);
    890:         path[0] = swapToken;
    891:         path[1] = desiredToken;
    892: 
```

#### Line 894 (L886–L902)
```solidity
    886:         _removeLiqudity(address(pair), address(this));
    887: 
    888:         address swapToken = token1 == desiredToken ? token0 : token1;
    889:         address[] memory path = new address[](2);
    890:         path[0] = swapToken;
    891:         path[1] = desiredToken;
    892: 
    893:         _approveTokenIfNeeded(path[0], address(router));
>>  894:         router.swapExactTokensForTokens(IERC20(swapToken).balanceOf(address(this)), desiredTokenOutMin, path, address(this), block.timestamp);
    895: 
    896:         _returnAssets(path);
    897:     }
    898: 
    899:     function _removeLiqudity(address pair, address to) private {
    900:         IERC20(pair).safeTransfer(pair, IERC20(pair).balanceOf(address(this)));
    901:         (uint256 amount0, uint256 amount1) = IUniswapV2Pair(pair).burn(to);
    902: 
```

#### Line 900 (L892–L908)
```solidity
    892: 
    893:         _approveTokenIfNeeded(path[0], address(router));
    894:         router.swapExactTokensForTokens(IERC20(swapToken).balanceOf(address(this)), desiredTokenOutMin, path, address(this), block.timestamp);
    895: 
    896:         _returnAssets(path);
    897:     }
    898: 
    899:     function _removeLiqudity(address pair, address to) private {
>>  900:         IERC20(pair).safeTransfer(pair, IERC20(pair).balanceOf(address(this)));
    901:         (uint256 amount0, uint256 amount1) = IUniswapV2Pair(pair).burn(to);
    902: 
    903:         require(amount0 >= minimumAmount, 'UniswapV2Router: INSUFFICIENT_A_AMOUNT');
    904:         require(amount1 >= minimumAmount, 'UniswapV2Router: INSUFFICIENT_B_AMOUNT');
    905:     }
    906: 
    907:     function _getVaultPair (address beefyVault) private view returns (IBeefyVaultV6 vault, IUniswapV2Pair pair) {
    908:         vault = IBeefyVaultV6(beefyVault);
```

#### Line 916 (L908–L924)
```solidity
    908:         vault = IBeefyVaultV6(beefyVault);
    909:         pair = IUniswapV2Pair(vault.want());
    910:         require(pair.factory() == router.factory(), 'Beefy: Incompatible liquidity pair factory');
    911:     }
    912: 
    913:     function _swapAndStake(address beefyVault, uint256 tokenAmountOutMin, address tokenIn) private {
    914:         (IBeefyVaultV6 vault, IUniswapV2Pair pair) = _getVaultPair(beefyVault);
    915: 
>>  916:         (uint256 reserveA, uint256 reserveB,) = pair.getReserves();
    917:         require(reserveA > minimumAmount && reserveB > minimumAmount, 'Beefy: Liquidity pair reserves too low');
    918: 
    919:         bool isInputA = pair.token0() == tokenIn;
    920:         require(isInputA || pair.token1() == tokenIn, 'Beefy: Input token not present in liqudity pair');
    921: 
    922:         address[] memory path = new address[](2);
    923:         path[0] = tokenIn;
    924:         path[1] = isInputA ? pair.token1() : pair.token0();
```

#### Line 926 (L918–L934)
```solidity
    918: 
    919:         bool isInputA = pair.token0() == tokenIn;
    920:         require(isInputA || pair.token1() == tokenIn, 'Beefy: Input token not present in liqudity pair');
    921: 
    922:         address[] memory path = new address[](2);
    923:         path[0] = tokenIn;
    924:         path[1] = isInputA ? pair.token1() : pair.token0();
    925: 
>>  926:         uint256 fullInvestment = IERC20(tokenIn).balanceOf(address(this));
    927:         uint256 swapAmountIn;
    928:         if (isInputA) {
    929:             swapAmountIn = _getSwapAmount(fullInvestment, reserveA, reserveB);
    930:         } else {
    931:             swapAmountIn = _getSwapAmount(fullInvestment, reserveB, reserveA);
    932:         }
    933: 
    934:         _approveTokenIfNeeded(path[0], address(router));
```

#### Line 936 (L928–L944)
```solidity
    928:         if (isInputA) {
    929:             swapAmountIn = _getSwapAmount(fullInvestment, reserveA, reserveB);
    930:         } else {
    931:             swapAmountIn = _getSwapAmount(fullInvestment, reserveB, reserveA);
    932:         }
    933: 
    934:         _approveTokenIfNeeded(path[0], address(router));
    935:         uint256[] memory swapedAmounts = router
>>  936:             .swapExactTokensForTokens(swapAmountIn, tokenAmountOutMin, path, address(this), block.timestamp);
    937: 
    938:         _approveTokenIfNeeded(path[1], address(router));
    939:         (,, uint256 amountLiquidity) = router
    940:             .addLiquidity(path[0], path[1], fullInvestment.sub(swapedAmounts[0]), swapedAmounts[1], 1, 1, address(this), block.timestamp);
    941: 
    942:         _approveTokenIfNeeded(address(pair), address(vault));
    943:         vault.deposit(amountLiquidity);
    944: 
```

#### Line 940 (L932–L948)
```solidity
    932:         }
    933: 
    934:         _approveTokenIfNeeded(path[0], address(router));
    935:         uint256[] memory swapedAmounts = router
    936:             .swapExactTokensForTokens(swapAmountIn, tokenAmountOutMin, path, address(this), block.timestamp);
    937: 
    938:         _approveTokenIfNeeded(path[1], address(router));
    939:         (,, uint256 amountLiquidity) = router
>>  940:             .addLiquidity(path[0], path[1], fullInvestment.sub(swapedAmounts[0]), swapedAmounts[1], 1, 1, address(this), block.timestamp);
    941: 
    942:         _approveTokenIfNeeded(address(pair), address(vault));
    943:         vault.deposit(amountLiquidity);
    944: 
    945:         vault.safeTransfer(msg.sender, vault.balanceOf(address(this)));
    946:         _returnAssets(path);
    947:     }
    948: 
```

#### Line 945 (L937–L953)
```solidity
    937: 
    938:         _approveTokenIfNeeded(path[1], address(router));
    939:         (,, uint256 amountLiquidity) = router
    940:             .addLiquidity(path[0], path[1], fullInvestment.sub(swapedAmounts[0]), swapedAmounts[1], 1, 1, address(this), block.timestamp);
    941: 
    942:         _approveTokenIfNeeded(address(pair), address(vault));
    943:         vault.deposit(amountLiquidity);
    944: 
>>  945:         vault.safeTransfer(msg.sender, vault.balanceOf(address(this)));
    946:         _returnAssets(path);
    947:     }
    948: 
    949:     function _returnAssets(address[] memory tokens) private {
    950:         uint256 balance;
    951:         for (uint256 i; i < tokens.length; i++) {
    952:             balance = IERC20(tokens[i]).balanceOf(address(this));
    953:             if (balance > 0) {
```

#### Line 952 (L944–L960)
```solidity
    944: 
    945:         vault.safeTransfer(msg.sender, vault.balanceOf(address(this)));
    946:         _returnAssets(path);
    947:     }
    948: 
    949:     function _returnAssets(address[] memory tokens) private {
    950:         uint256 balance;
    951:         for (uint256 i; i < tokens.length; i++) {
>>  952:             balance = IERC20(tokens[i]).balanceOf(address(this));
    953:             if (balance > 0) {
    954:                 if (tokens[i] == WETH) {
    955:                     IWETH(WETH).withdraw(balance);
    956:                     (bool success,) = msg.sender.call{value: balance}(new bytes(0));
    957:                     require(success, 'Beefy: ETH transfer failed');
    958:                 } else {
    959:                     IERC20(tokens[i]).safeTransfer(msg.sender, balance);
    960:                 }
```

#### Line 959 (L951–L967)
```solidity
    951:         for (uint256 i; i < tokens.length; i++) {
    952:             balance = IERC20(tokens[i]).balanceOf(address(this));
    953:             if (balance > 0) {
    954:                 if (tokens[i] == WETH) {
    955:                     IWETH(WETH).withdraw(balance);
    956:                     (bool success,) = msg.sender.call{value: balance}(new bytes(0));
    957:                     require(success, 'Beefy: ETH transfer failed');
    958:                 } else {
>>  959:                     IERC20(tokens[i]).safeTransfer(msg.sender, balance);
    960:                 }
    961:             }
    962:         }
    963:     }
    964: 
    965:     function _getSwapAmount(uint256 investmentA, uint256 reserveA, uint256 reserveB) private view returns (uint256 swapAmount) {
    966:         uint256 halfInvestment = investmentA / 2;
    967:         uint256 nominator = router.getAmountOut(halfInvestment, reserveA, reserveB);
```

#### Line 979 (L971–L987)
```solidity
    971: 
    972:     function estimateSwap(address beefyVault, address tokenIn, uint256 fullInvestmentIn) public view returns(uint256 swapAmountIn, uint256 swapAmountOut, address swapTokenOut) {
    973:         checkWETH();
    974:         (, IUniswapV2Pair pair) = _getVaultPair(beefyVault);
    975: 
    976:         bool isInputA = pair.token0() == tokenIn;
    977:         require(isInputA || pair.token1() == tokenIn, 'Beefy: Input token not present in liqudity pair');
    978: 
>>  979:         (uint256 reserveA, uint256 reserveB,) = pair.getReserves();
    980:         (reserveA, reserveB) = isInputA ? (reserveA, reserveB) : (reserveB, reserveA);
    981: 
    982:         swapAmountIn = _getSwapAmount(fullInvestmentIn, reserveA, reserveB);
    983:         swapAmountOut = router.getAmountOut(swapAmountIn, reserveA, reserveB);
    984:         swapTokenOut = isInputA ? pair.token1() : pair.token0();
    985:     }
    986: 
    987:     function checkWETH() public view returns (bool isValid) {
```

#### Line 994 (L986–L998)
```solidity
    986: 
    987:     function checkWETH() public view returns (bool isValid) {
    988:         isValid = WETH == router.WETH();
    989:         require(isValid, 'Beefy: WETH address not matching Router.WETH()');
    990:     }
    991: 
    992:     function _approveTokenIfNeeded(address token, address spender) private {
    993:         if (IERC20(token).allowance(address(this), spender) == 0) {
>>  994:             IERC20(token).safeApprove(spender, type(uint).max);
    995:         }
    996:     }
    997: 
    998: }
```

## `contracts/archive/strategies/Cometh/StrategyMultiRewardsPolygonLP.sol` (442 lines)
### Functions / Constructors
- L83: `constructor` — `constructor(          address _want,          address _rewardPool,`
- L159: `deposit` — `function deposit() public whenNotPaused {          uint256 wantBal = IERC20(want).balanceOf(address(this));`
- L175: `withdraw` — `function withdraw(uint256 _amount) external {          require(msg.sender == vault, "!vault");`
- L221: `harvest` — `function harvest() external whenNotPaused {          IRewardPool(rewardPool).getReward();          chargeFees();`
- L241: `chargeFees` — `function chargeFees() internal {          uint256 toOutput = IERC20(secondOutput).balanceOf(address(this));          IUniswapRouterETH(unirouter).swapExactToken`
- L281: `addLiquidity` — `function addLiquidity() internal {          uint256 outputHalf = IERC20(output).balanceOf(address(this)).div(2);`
- L315: `balanceOf` — `function balanceOf() public view returns (uint256) {          return balanceOfWant().add(balanceOfPool());      }`
- L325: `balanceOfWant` — `function balanceOfWant() public view returns (uint256) {          return IERC20(want).balanceOf(address(this));      }`
- L335: `balanceOfPool` — `function balanceOfPool() public view returns (uint256) {          return IRewardPool(rewardPool).balanceOf(address(this));      }`
- L345: `retireStrat` — `function retireStrat() external {          require(msg.sender == vault, "!vault");`
- L365: `panic` — `function panic() public onlyManager {          pause();          IRewardPool(rewardPool).withdraw(balanceOfPool());`
- L375: `pause` — `function pause() public onlyManager {          _pause();`
- L387: `unpause` — `function unpause() external onlyManager {          _unpause();`
- L403: `_giveAllowances` — `function _giveAllowances() internal {          IERC20(want).safeApprove(rewardPool, uint256(-1));          IERC20(output).safeApprove(unirouter, uint256(-1));`
- L427: `_removeAllowances` — `function _removeAllowances() internal {          IERC20(want).safeApprove(rewardPool, 0);          IERC20(output).safeApprove(unirouter, 0);`

### Sink Windows (±8 lines)
#### Line 161 (L153–L169)
```solidity
    153:     }
    154: 
    155: 
    156: 
    157:     // puts the funds to work
    158: 
    159:     function deposit() public whenNotPaused {
    160: 
>>  161:         uint256 wantBal = IERC20(want).balanceOf(address(this));
    162: 
    163: 
    164: 
    165:         if (wantBal > 0) {
    166: 
    167:             IRewardPool(rewardPool).stake(wantBal);
    168: 
    169:         }
```

#### Line 181 (L173–L189)
```solidity
    173: 
    174: 
    175:     function withdraw(uint256 _amount) external {
    176: 
    177:         require(msg.sender == vault, "!vault");
    178: 
    179: 
    180: 
>>  181:         uint256 wantBal = IERC20(want).balanceOf(address(this));
    182: 
    183: 
    184: 
    185:         if (wantBal < _amount) {
    186: 
    187:             IRewardPool(rewardPool).withdraw(_amount.sub(wantBal));
    188: 
    189:             wantBal = IERC20(want).balanceOf(address(this));
```

#### Line 189 (L181–L197)
```solidity
    181:         uint256 wantBal = IERC20(want).balanceOf(address(this));
    182: 
    183: 
    184: 
    185:         if (wantBal < _amount) {
    186: 
    187:             IRewardPool(rewardPool).withdraw(_amount.sub(wantBal));
    188: 
>>  189:             wantBal = IERC20(want).balanceOf(address(this));
    190: 
    191:         }
    192: 
    193: 
    194: 
    195:         if (wantBal > _amount) {
    196: 
    197:             wantBal = _amount;
```

#### Line 205 (L197–L213)
```solidity
    197:             wantBal = _amount;
    198: 
    199:         }
    200: 
    201: 
    202: 
    203:         if (tx.origin == owner() || paused()) {
    204: 
>>  205:             IERC20(want).safeTransfer(vault, wantBal);
    206: 
    207:         } else {
    208: 
    209:             uint256 withdrawalFee = wantBal.mul(WITHDRAWAL_FEE_CAP).div(WITHDRAWAL_MAX);
    210: 
    211:             IERC20(want).safeTransfer(vault, wantBal.sub(withdrawalFee));
    212: 
    213:         }
```

#### Line 211 (L203–L219)
```solidity
    203:         if (tx.origin == owner() || paused()) {
    204: 
    205:             IERC20(want).safeTransfer(vault, wantBal);
    206: 
    207:         } else {
    208: 
    209:             uint256 withdrawalFee = wantBal.mul(WITHDRAWAL_FEE_CAP).div(WITHDRAWAL_MAX);
    210: 
>>  211:             IERC20(want).safeTransfer(vault, wantBal.sub(withdrawalFee));
    212: 
    213:         }
    214: 
    215:     }
    216: 
    217: 
    218: 
    219:     // compounds earnings and charges performance fee
```

#### Line 227 (L219–L235)
```solidity
    219:     // compounds earnings and charges performance fee
    220: 
    221:     function harvest() external whenNotPaused {
    222: 
    223:         IRewardPool(rewardPool).getReward();
    224: 
    225:         chargeFees();
    226: 
>>  227:         addLiquidity();
    228: 
    229:         deposit();
    230: 
    231: 
    232: 
    233:         emit StratHarvest(msg.sender);
    234: 
    235:     }
```

#### Line 243 (L235–L251)
```solidity
    235:     }
    236: 
    237: 
    238: 
    239:     // performance fees
    240: 
    241:     function chargeFees() internal {
    242: 
>>  243:         uint256 toOutput = IERC20(secondOutput).balanceOf(address(this));
    244: 
    245:         IUniswapRouterETH(unirouter).swapExactTokensForTokens(toOutput, 0, secondOutputToOutputRoute, address(this), now);
    246: 
    247:         
    248: 
    249:         uint256 toMatic = IERC20(output).balanceOf(address(this)).mul(45).div(1000);
    250: 
    251:         IUniswapRouterETH(unirouter).swapExactTokensForTokens(toMatic, 0, outputToMaticRoute, address(this), now);
```

#### Line 245 (L237–L253)
```solidity
    237: 
    238: 
    239:     // performance fees
    240: 
    241:     function chargeFees() internal {
    242: 
    243:         uint256 toOutput = IERC20(secondOutput).balanceOf(address(this));
    244: 
>>  245:         IUniswapRouterETH(unirouter).swapExactTokensForTokens(toOutput, 0, secondOutputToOutputRoute, address(this), now);
    246: 
    247:         
    248: 
    249:         uint256 toMatic = IERC20(output).balanceOf(address(this)).mul(45).div(1000);
    250: 
    251:         IUniswapRouterETH(unirouter).swapExactTokensForTokens(toMatic, 0, outputToMaticRoute, address(this), now);
    252: 
    253: 
```

#### Line 249 (L241–L257)
```solidity
    241:     function chargeFees() internal {
    242: 
    243:         uint256 toOutput = IERC20(secondOutput).balanceOf(address(this));
    244: 
    245:         IUniswapRouterETH(unirouter).swapExactTokensForTokens(toOutput, 0, secondOutputToOutputRoute, address(this), now);
    246: 
    247:         
    248: 
>>  249:         uint256 toMatic = IERC20(output).balanceOf(address(this)).mul(45).div(1000);
    250: 
    251:         IUniswapRouterETH(unirouter).swapExactTokensForTokens(toMatic, 0, outputToMaticRoute, address(this), now);
    252: 
    253: 
    254: 
    255:         uint256 maticBal = IERC20(matic).balanceOf(address(this));
    256: 
    257: 
```

#### Line 251 (L243–L259)
```solidity
    243:         uint256 toOutput = IERC20(secondOutput).balanceOf(address(this));
    244: 
    245:         IUniswapRouterETH(unirouter).swapExactTokensForTokens(toOutput, 0, secondOutputToOutputRoute, address(this), now);
    246: 
    247:         
    248: 
    249:         uint256 toMatic = IERC20(output).balanceOf(address(this)).mul(45).div(1000);
    250: 
>>  251:         IUniswapRouterETH(unirouter).swapExactTokensForTokens(toMatic, 0, outputToMaticRoute, address(this), now);
    252: 
    253: 
    254: 
    255:         uint256 maticBal = IERC20(matic).balanceOf(address(this));
    256: 
    257: 
    258: 
    259:         uint256 callFeeAmount = maticBal.mul(callFee).div(MAX_FEE);
```

#### Line 255 (L247–L263)
```solidity
    247:         
    248: 
    249:         uint256 toMatic = IERC20(output).balanceOf(address(this)).mul(45).div(1000);
    250: 
    251:         IUniswapRouterETH(unirouter).swapExactTokensForTokens(toMatic, 0, outputToMaticRoute, address(this), now);
    252: 
    253: 
    254: 
>>  255:         uint256 maticBal = IERC20(matic).balanceOf(address(this));
    256: 
    257: 
    258: 
    259:         uint256 callFeeAmount = maticBal.mul(callFee).div(MAX_FEE);
    260: 
    261:         IERC20(matic).safeTransfer(tx.origin, callFeeAmount);
    262: 
    263: 
```

#### Line 261 (L253–L269)
```solidity
    253: 
    254: 
    255:         uint256 maticBal = IERC20(matic).balanceOf(address(this));
    256: 
    257: 
    258: 
    259:         uint256 callFeeAmount = maticBal.mul(callFee).div(MAX_FEE);
    260: 
>>  261:         IERC20(matic).safeTransfer(tx.origin, callFeeAmount);
    262: 
    263: 
    264: 
    265:         uint256 beefyFeeAmount = maticBal.mul(beefyFee).div(MAX_FEE);
    266: 
    267:         IERC20(matic).safeTransfer(beefyFeeRecipient, beefyFeeAmount);
    268: 
    269: 
```

#### Line 267 (L259–L275)
```solidity
    259:         uint256 callFeeAmount = maticBal.mul(callFee).div(MAX_FEE);
    260: 
    261:         IERC20(matic).safeTransfer(tx.origin, callFeeAmount);
    262: 
    263: 
    264: 
    265:         uint256 beefyFeeAmount = maticBal.mul(beefyFee).div(MAX_FEE);
    266: 
>>  267:         IERC20(matic).safeTransfer(beefyFeeRecipient, beefyFeeAmount);
    268: 
    269: 
    270: 
    271:         uint256 strategistFee = maticBal.mul(STRATEGIST_FEE).div(MAX_FEE);
    272: 
    273:         IERC20(matic).safeTransfer(strategist, strategistFee);
    274: 
    275:     }
```

#### Line 273 (L265–L281)
```solidity
    265:         uint256 beefyFeeAmount = maticBal.mul(beefyFee).div(MAX_FEE);
    266: 
    267:         IERC20(matic).safeTransfer(beefyFeeRecipient, beefyFeeAmount);
    268: 
    269: 
    270: 
    271:         uint256 strategistFee = maticBal.mul(STRATEGIST_FEE).div(MAX_FEE);
    272: 
>>  273:         IERC20(matic).safeTransfer(strategist, strategistFee);
    274: 
    275:     }
    276: 
    277: 
    278: 
    279:     // Adds liquidity to AMM and gets more LP tokens.
    280: 
    281:     function addLiquidity() internal {
```

#### Line 281 (L273–L289)
```solidity
    273:         IERC20(matic).safeTransfer(strategist, strategistFee);
    274: 
    275:     }
    276: 
    277: 
    278: 
    279:     // Adds liquidity to AMM and gets more LP tokens.
    280: 
>>  281:     function addLiquidity() internal {
    282: 
    283:         uint256 outputHalf = IERC20(output).balanceOf(address(this)).div(2);
    284: 
    285: 
    286: 
    287:         if (lpToken0 != output) {
    288: 
    289:             IUniswapRouterETH(unirouter).swapExactTokensForTokens(outputHalf, 0, outputToLp0Route, address(this), now);
```

#### Line 283 (L275–L291)
```solidity
    275:     }
    276: 
    277: 
    278: 
    279:     // Adds liquidity to AMM and gets more LP tokens.
    280: 
    281:     function addLiquidity() internal {
    282: 
>>  283:         uint256 outputHalf = IERC20(output).balanceOf(address(this)).div(2);
    284: 
    285: 
    286: 
    287:         if (lpToken0 != output) {
    288: 
    289:             IUniswapRouterETH(unirouter).swapExactTokensForTokens(outputHalf, 0, outputToLp0Route, address(this), now);
    290: 
    291:         }
```

#### Line 289 (L281–L297)
```solidity
    281:     function addLiquidity() internal {
    282: 
    283:         uint256 outputHalf = IERC20(output).balanceOf(address(this)).div(2);
    284: 
    285: 
    286: 
    287:         if (lpToken0 != output) {
    288: 
>>  289:             IUniswapRouterETH(unirouter).swapExactTokensForTokens(outputHalf, 0, outputToLp0Route, address(this), now);
    290: 
    291:         }
    292: 
    293: 
    294: 
    295:         if (lpToken1 != output) {
    296: 
    297:             IUniswapRouterETH(unirouter).swapExactTokensForTokens(outputHalf, 0, outputToLp1Route, address(this), now);
```

#### Line 297 (L289–L305)
```solidity
    289:             IUniswapRouterETH(unirouter).swapExactTokensForTokens(outputHalf, 0, outputToLp0Route, address(this), now);
    290: 
    291:         }
    292: 
    293: 
    294: 
    295:         if (lpToken1 != output) {
    296: 
>>  297:             IUniswapRouterETH(unirouter).swapExactTokensForTokens(outputHalf, 0, outputToLp1Route, address(this), now);
    298: 
    299:         }
    300: 
    301: 
    302: 
    303:         uint256 lp0Bal = IERC20(lpToken0).balanceOf(address(this));
    304: 
    305:         uint256 lp1Bal = IERC20(lpToken1).balanceOf(address(this));
```

#### Line 303 (L295–L311)
```solidity
    295:         if (lpToken1 != output) {
    296: 
    297:             IUniswapRouterETH(unirouter).swapExactTokensForTokens(outputHalf, 0, outputToLp1Route, address(this), now);
    298: 
    299:         }
    300: 
    301: 
    302: 
>>  303:         uint256 lp0Bal = IERC20(lpToken0).balanceOf(address(this));
    304: 
    305:         uint256 lp1Bal = IERC20(lpToken1).balanceOf(address(this));
    306: 
    307:         IUniswapRouterETH(unirouter).addLiquidity(lpToken0, lpToken1, lp0Bal, lp1Bal, 1, 1, address(this), now);
    308: 
    309:     }
    310: 
    311: 
```

#### Line 305 (L297–L313)
```solidity
    297:             IUniswapRouterETH(unirouter).swapExactTokensForTokens(outputHalf, 0, outputToLp1Route, address(this), now);
    298: 
    299:         }
    300: 
    301: 
    302: 
    303:         uint256 lp0Bal = IERC20(lpToken0).balanceOf(address(this));
    304: 
>>  305:         uint256 lp1Bal = IERC20(lpToken1).balanceOf(address(this));
    306: 
    307:         IUniswapRouterETH(unirouter).addLiquidity(lpToken0, lpToken1, lp0Bal, lp1Bal, 1, 1, address(this), now);
    308: 
    309:     }
    310: 
    311: 
    312: 
    313:     // calculate the total underlaying 'want' held by the strat.
```

#### Line 307 (L299–L315)
```solidity
    299:         }
    300: 
    301: 
    302: 
    303:         uint256 lp0Bal = IERC20(lpToken0).balanceOf(address(this));
    304: 
    305:         uint256 lp1Bal = IERC20(lpToken1).balanceOf(address(this));
    306: 
>>  307:         IUniswapRouterETH(unirouter).addLiquidity(lpToken0, lpToken1, lp0Bal, lp1Bal, 1, 1, address(this), now);
    308: 
    309:     }
    310: 
    311: 
    312: 
    313:     // calculate the total underlaying 'want' held by the strat.
    314: 
    315:     function balanceOf() public view returns (uint256) {
```

#### Line 315 (L307–L323)
```solidity
    307:         IUniswapRouterETH(unirouter).addLiquidity(lpToken0, lpToken1, lp0Bal, lp1Bal, 1, 1, address(this), now);
    308: 
    309:     }
    310: 
    311: 
    312: 
    313:     // calculate the total underlaying 'want' held by the strat.
    314: 
>>  315:     function balanceOf() public view returns (uint256) {
    316: 
    317:         return balanceOfWant().add(balanceOfPool());
    318: 
    319:     }
    320: 
    321: 
    322: 
    323:     // it calculates how much 'want' this contract holds.
```

#### Line 327 (L319–L335)
```solidity
    319:     }
    320: 
    321: 
    322: 
    323:     // it calculates how much 'want' this contract holds.
    324: 
    325:     function balanceOfWant() public view returns (uint256) {
    326: 
>>  327:         return IERC20(want).balanceOf(address(this));
    328: 
    329:     }
    330: 
    331: 
    332: 
    333:     // it calculates how much 'want' the strategy has working in the farm.
    334: 
    335:     function balanceOfPool() public view returns (uint256) {
```

#### Line 337 (L329–L345)
```solidity
    329:     }
    330: 
    331: 
    332: 
    333:     // it calculates how much 'want' the strategy has working in the farm.
    334: 
    335:     function balanceOfPool() public view returns (uint256) {
    336: 
>>  337:         return IRewardPool(rewardPool).balanceOf(address(this));
    338: 
    339:     }
    340: 
    341: 
    342: 
    343:     // called as part of strat migration. Sends all the available funds back to the vault.
    344: 
    345:     function retireStrat() external {
```

#### Line 355 (L347–L363)
```solidity
    347:         require(msg.sender == vault, "!vault");
    348: 
    349: 
    350: 
    351:         IRewardPool(rewardPool).withdraw(balanceOfPool());
    352: 
    353: 
    354: 
>>  355:         uint256 wantBal = IERC20(want).balanceOf(address(this));
    356: 
    357:         IERC20(want).transfer(vault, wantBal);
    358: 
    359:     }
    360: 
    361: 
    362: 
    363:     // pauses deposits and withdraws all funds from third party systems.
```

#### Line 405 (L397–L413)
```solidity
    397:         deposit();
    398: 
    399:     }
    400: 
    401: 
    402: 
    403:     function _giveAllowances() internal {
    404: 
>>  405:         IERC20(want).safeApprove(rewardPool, uint256(-1));
    406: 
    407:         IERC20(output).safeApprove(unirouter, uint256(-1));
    408: 
    409:         IERC20(secondOutput).safeApprove(unirouter, uint256(-1));
    410: 
    411: 
    412: 
    413:         IERC20(lpToken0).safeApprove(unirouter, 0);
```

#### Line 407 (L399–L415)
```solidity
    399:     }
    400: 
    401: 
    402: 
    403:     function _giveAllowances() internal {
    404: 
    405:         IERC20(want).safeApprove(rewardPool, uint256(-1));
    406: 
>>  407:         IERC20(output).safeApprove(unirouter, uint256(-1));
    408: 
    409:         IERC20(secondOutput).safeApprove(unirouter, uint256(-1));
    410: 
    411: 
    412: 
    413:         IERC20(lpToken0).safeApprove(unirouter, 0);
    414: 
    415:         IERC20(lpToken0).safeApprove(unirouter, uint256(-1));
```

#### Line 409 (L401–L417)
```solidity
    401: 
    402: 
    403:     function _giveAllowances() internal {
    404: 
    405:         IERC20(want).safeApprove(rewardPool, uint256(-1));
    406: 
    407:         IERC20(output).safeApprove(unirouter, uint256(-1));
    408: 
>>  409:         IERC20(secondOutput).safeApprove(unirouter, uint256(-1));
    410: 
    411: 
    412: 
    413:         IERC20(lpToken0).safeApprove(unirouter, 0);
    414: 
    415:         IERC20(lpToken0).safeApprove(unirouter, uint256(-1));
    416: 
    417: 
```

#### Line 413 (L405–L421)
```solidity
    405:         IERC20(want).safeApprove(rewardPool, uint256(-1));
    406: 
    407:         IERC20(output).safeApprove(unirouter, uint256(-1));
    408: 
    409:         IERC20(secondOutput).safeApprove(unirouter, uint256(-1));
    410: 
    411: 
    412: 
>>  413:         IERC20(lpToken0).safeApprove(unirouter, 0);
    414: 
    415:         IERC20(lpToken0).safeApprove(unirouter, uint256(-1));
    416: 
    417: 
    418: 
    419:         IERC20(lpToken1).safeApprove(unirouter, 0);
    420: 
    421:         IERC20(lpToken1).safeApprove(unirouter, uint256(-1));
```

#### Line 415 (L407–L423)
```solidity
    407:         IERC20(output).safeApprove(unirouter, uint256(-1));
    408: 
    409:         IERC20(secondOutput).safeApprove(unirouter, uint256(-1));
    410: 
    411: 
    412: 
    413:         IERC20(lpToken0).safeApprove(unirouter, 0);
    414: 
>>  415:         IERC20(lpToken0).safeApprove(unirouter, uint256(-1));
    416: 
    417: 
    418: 
    419:         IERC20(lpToken1).safeApprove(unirouter, 0);
    420: 
    421:         IERC20(lpToken1).safeApprove(unirouter, uint256(-1));
    422: 
    423:     }
```

#### Line 419 (L411–L427)
```solidity
    411: 
    412: 
    413:         IERC20(lpToken0).safeApprove(unirouter, 0);
    414: 
    415:         IERC20(lpToken0).safeApprove(unirouter, uint256(-1));
    416: 
    417: 
    418: 
>>  419:         IERC20(lpToken1).safeApprove(unirouter, 0);
    420: 
    421:         IERC20(lpToken1).safeApprove(unirouter, uint256(-1));
    422: 
    423:     }
    424: 
    425: 
    426: 
    427:     function _removeAllowances() internal {
```

#### Line 421 (L413–L429)
```solidity
    413:         IERC20(lpToken0).safeApprove(unirouter, 0);
    414: 
    415:         IERC20(lpToken0).safeApprove(unirouter, uint256(-1));
    416: 
    417: 
    418: 
    419:         IERC20(lpToken1).safeApprove(unirouter, 0);
    420: 
>>  421:         IERC20(lpToken1).safeApprove(unirouter, uint256(-1));
    422: 
    423:     }
    424: 
    425: 
    426: 
    427:     function _removeAllowances() internal {
    428: 
    429:         IERC20(want).safeApprove(rewardPool, 0);
```

#### Line 429 (L421–L437)
```solidity
    421:         IERC20(lpToken1).safeApprove(unirouter, uint256(-1));
    422: 
    423:     }
    424: 
    425: 
    426: 
    427:     function _removeAllowances() internal {
    428: 
>>  429:         IERC20(want).safeApprove(rewardPool, 0);
    430: 
    431:         IERC20(output).safeApprove(unirouter, 0);
    432: 
    433:         IERC20(secondOutput).safeApprove(unirouter, 0);
    434: 
    435:         IERC20(lpToken0).safeApprove(unirouter, 0);
    436: 
    437:         IERC20(lpToken1).safeApprove(unirouter, 0);
```

#### Line 431 (L423–L439)
```solidity
    423:     }
    424: 
    425: 
    426: 
    427:     function _removeAllowances() internal {
    428: 
    429:         IERC20(want).safeApprove(rewardPool, 0);
    430: 
>>  431:         IERC20(output).safeApprove(unirouter, 0);
    432: 
    433:         IERC20(secondOutput).safeApprove(unirouter, 0);
    434: 
    435:         IERC20(lpToken0).safeApprove(unirouter, 0);
    436: 
    437:         IERC20(lpToken1).safeApprove(unirouter, 0);
    438: 
    439:     }
```

#### Line 433 (L425–L441)
```solidity
    425: 
    426: 
    427:     function _removeAllowances() internal {
    428: 
    429:         IERC20(want).safeApprove(rewardPool, 0);
    430: 
    431:         IERC20(output).safeApprove(unirouter, 0);
    432: 
>>  433:         IERC20(secondOutput).safeApprove(unirouter, 0);
    434: 
    435:         IERC20(lpToken0).safeApprove(unirouter, 0);
    436: 
    437:         IERC20(lpToken1).safeApprove(unirouter, 0);
    438: 
    439:     }
    440: 
    441: }
```

#### Line 435 (L427–L442)
```solidity
    427:     function _removeAllowances() internal {
    428: 
    429:         IERC20(want).safeApprove(rewardPool, 0);
    430: 
    431:         IERC20(output).safeApprove(unirouter, 0);
    432: 
    433:         IERC20(secondOutput).safeApprove(unirouter, 0);
    434: 
>>  435:         IERC20(lpToken0).safeApprove(unirouter, 0);
    436: 
    437:         IERC20(lpToken1).safeApprove(unirouter, 0);
    438: 
    439:     }
    440: 
    441: }
    442: 
```

#### Line 437 (L429–L442)
```solidity
    429:         IERC20(want).safeApprove(rewardPool, 0);
    430: 
    431:         IERC20(output).safeApprove(unirouter, 0);
    432: 
    433:         IERC20(secondOutput).safeApprove(unirouter, 0);
    434: 
    435:         IERC20(lpToken0).safeApprove(unirouter, 0);
    436: 
>>  437:         IERC20(lpToken1).safeApprove(unirouter, 0);
    438: 
    439:     }
    440: 
    441: }
    442: 
```

## `contracts/archive/strategies/Cometh/StrategyRewardPoolPolygonLP.sol` (420 lines)
### Functions / Constructors
- L79: `constructor` — `constructor(          address _want,          address _rewardPool,`
- L147: `deposit` — `function deposit() public whenNotPaused {          uint256 wantBal = IERC20(want).balanceOf(address(this));`
- L163: `withdraw` — `function withdraw(uint256 _amount) external {          require(msg.sender == vault, "!vault");`
- L209: `harvest` — `function harvest() external whenNotPaused {          IRewardPool(rewardPool).getReward();          chargeFees();`
- L229: `chargeFees` — `function chargeFees() internal {          uint256 toMatic = IERC20(output).balanceOf(address(this)).mul(45).div(1000);          IUniswapRouterETH(unirouter).swa`
- L263: `addLiquidity` — `function addLiquidity() internal {          uint256 outputHalf = IERC20(output).balanceOf(address(this)).div(2);`
- L297: `balanceOf` — `function balanceOf() public view returns (uint256) {          return balanceOfWant().add(balanceOfPool());      }`
- L307: `balanceOfWant` — `function balanceOfWant() public view returns (uint256) {          return IERC20(want).balanceOf(address(this));      }`
- L317: `balanceOfPool` — `function balanceOfPool() public view returns (uint256) {          return IRewardPool(rewardPool).balanceOf(address(this));      }`
- L327: `retireStrat` — `function retireStrat() external {          require(msg.sender == vault, "!vault");`
- L347: `panic` — `function panic() public onlyManager {          pause();          IRewardPool(rewardPool).withdraw(balanceOfPool());`
- L357: `pause` — `function pause() public onlyManager {          _pause();`
- L369: `unpause` — `function unpause() external onlyManager {          _unpause();`
- L385: `_giveAllowances` — `function _giveAllowances() internal {          IERC20(want).safeApprove(rewardPool, uint256(-1));          IERC20(output).safeApprove(unirouter, uint256(-1));`
- L407: `_removeAllowances` — `function _removeAllowances() internal {          IERC20(want).safeApprove(rewardPool, 0);          IERC20(output).safeApprove(unirouter, 0);`

### Sink Windows (±8 lines)
#### Line 149 (L141–L157)
```solidity
    141:     }
    142: 
    143: 
    144: 
    145:     // puts the funds to work
    146: 
    147:     function deposit() public whenNotPaused {
    148: 
>>  149:         uint256 wantBal = IERC20(want).balanceOf(address(this));
    150: 
    151: 
    152: 
    153:         if (wantBal > 0) {
    154: 
    155:             IRewardPool(rewardPool).stake(wantBal);
    156: 
    157:         }
```

#### Line 169 (L161–L177)
```solidity
    161: 
    162: 
    163:     function withdraw(uint256 _amount) external {
    164: 
    165:         require(msg.sender == vault, "!vault");
    166: 
    167: 
    168: 
>>  169:         uint256 wantBal = IERC20(want).balanceOf(address(this));
    170: 
    171: 
    172: 
    173:         if (wantBal < _amount) {
    174: 
    175:             IRewardPool(rewardPool).withdraw(_amount.sub(wantBal));
    176: 
    177:             wantBal = IERC20(want).balanceOf(address(this));
```

#### Line 177 (L169–L185)
```solidity
    169:         uint256 wantBal = IERC20(want).balanceOf(address(this));
    170: 
    171: 
    172: 
    173:         if (wantBal < _amount) {
    174: 
    175:             IRewardPool(rewardPool).withdraw(_amount.sub(wantBal));
    176: 
>>  177:             wantBal = IERC20(want).balanceOf(address(this));
    178: 
    179:         }
    180: 
    181: 
    182: 
    183:         if (wantBal > _amount) {
    184: 
    185:             wantBal = _amount;
```

#### Line 193 (L185–L201)
```solidity
    185:             wantBal = _amount;
    186: 
    187:         }
    188: 
    189: 
    190: 
    191:         if (tx.origin == owner() || paused()) {
    192: 
>>  193:             IERC20(want).safeTransfer(vault, wantBal);
    194: 
    195:         } else {
    196: 
    197:             uint256 withdrawalFee = wantBal.mul(WITHDRAWAL_FEE_CAP).div(WITHDRAWAL_MAX);
    198: 
    199:             IERC20(want).safeTransfer(vault, wantBal.sub(withdrawalFee));
    200: 
    201:         }
```

#### Line 199 (L191–L207)
```solidity
    191:         if (tx.origin == owner() || paused()) {
    192: 
    193:             IERC20(want).safeTransfer(vault, wantBal);
    194: 
    195:         } else {
    196: 
    197:             uint256 withdrawalFee = wantBal.mul(WITHDRAWAL_FEE_CAP).div(WITHDRAWAL_MAX);
    198: 
>>  199:             IERC20(want).safeTransfer(vault, wantBal.sub(withdrawalFee));
    200: 
    201:         }
    202: 
    203:     }
    204: 
    205: 
    206: 
    207:     // compounds earnings and charges performance fee
```

#### Line 215 (L207–L223)
```solidity
    207:     // compounds earnings and charges performance fee
    208: 
    209:     function harvest() external whenNotPaused {
    210: 
    211:         IRewardPool(rewardPool).getReward();
    212: 
    213:         chargeFees();
    214: 
>>  215:         addLiquidity();
    216: 
    217:         deposit();
    218: 
    219: 
    220: 
    221:         emit StratHarvest(msg.sender);
    222: 
    223:     }
```

#### Line 231 (L223–L239)
```solidity
    223:     }
    224: 
    225: 
    226: 
    227:     // performance fees
    228: 
    229:     function chargeFees() internal {
    230: 
>>  231:         uint256 toMatic = IERC20(output).balanceOf(address(this)).mul(45).div(1000);
    232: 
    233:         IUniswapRouterETH(unirouter).swapExactTokensForTokens(toMatic, 0, outputToMaticRoute, address(this), now);
    234: 
    235: 
    236: 
    237:         uint256 maticBal = IERC20(matic).balanceOf(address(this));
    238: 
    239: 
```

#### Line 233 (L225–L241)
```solidity
    225: 
    226: 
    227:     // performance fees
    228: 
    229:     function chargeFees() internal {
    230: 
    231:         uint256 toMatic = IERC20(output).balanceOf(address(this)).mul(45).div(1000);
    232: 
>>  233:         IUniswapRouterETH(unirouter).swapExactTokensForTokens(toMatic, 0, outputToMaticRoute, address(this), now);
    234: 
    235: 
    236: 
    237:         uint256 maticBal = IERC20(matic).balanceOf(address(this));
    238: 
    239: 
    240: 
    241:         uint256 callFeeAmount = maticBal.mul(callFee).div(MAX_FEE);
```

#### Line 237 (L229–L245)
```solidity
    229:     function chargeFees() internal {
    230: 
    231:         uint256 toMatic = IERC20(output).balanceOf(address(this)).mul(45).div(1000);
    232: 
    233:         IUniswapRouterETH(unirouter).swapExactTokensForTokens(toMatic, 0, outputToMaticRoute, address(this), now);
    234: 
    235: 
    236: 
>>  237:         uint256 maticBal = IERC20(matic).balanceOf(address(this));
    238: 
    239: 
    240: 
    241:         uint256 callFeeAmount = maticBal.mul(callFee).div(MAX_FEE);
    242: 
    243:         IERC20(matic).safeTransfer(tx.origin, callFeeAmount);
    244: 
    245: 
```

#### Line 243 (L235–L251)
```solidity
    235: 
    236: 
    237:         uint256 maticBal = IERC20(matic).balanceOf(address(this));
    238: 
    239: 
    240: 
    241:         uint256 callFeeAmount = maticBal.mul(callFee).div(MAX_FEE);
    242: 
>>  243:         IERC20(matic).safeTransfer(tx.origin, callFeeAmount);
    244: 
    245: 
    246: 
    247:         uint256 beefyFeeAmount = maticBal.mul(beefyFee).div(MAX_FEE);
    248: 
    249:         IERC20(matic).safeTransfer(beefyFeeRecipient, beefyFeeAmount);
    250: 
    251: 
```

#### Line 249 (L241–L257)
```solidity
    241:         uint256 callFeeAmount = maticBal.mul(callFee).div(MAX_FEE);
    242: 
    243:         IERC20(matic).safeTransfer(tx.origin, callFeeAmount);
    244: 
    245: 
    246: 
    247:         uint256 beefyFeeAmount = maticBal.mul(beefyFee).div(MAX_FEE);
    248: 
>>  249:         IERC20(matic).safeTransfer(beefyFeeRecipient, beefyFeeAmount);
    250: 
    251: 
    252: 
    253:         uint256 strategistFee = maticBal.mul(STRATEGIST_FEE).div(MAX_FEE);
    254: 
    255:         IERC20(matic).safeTransfer(strategist, strategistFee);
    256: 
    257:     }
```

#### Line 255 (L247–L263)
```solidity
    247:         uint256 beefyFeeAmount = maticBal.mul(beefyFee).div(MAX_FEE);
    248: 
    249:         IERC20(matic).safeTransfer(beefyFeeRecipient, beefyFeeAmount);
    250: 
    251: 
    252: 
    253:         uint256 strategistFee = maticBal.mul(STRATEGIST_FEE).div(MAX_FEE);
    254: 
>>  255:         IERC20(matic).safeTransfer(strategist, strategistFee);
    256: 
    257:     }
    258: 
    259: 
    260: 
    261:     // Adds liquidity to AMM and gets more LP tokens.
    262: 
    263:     function addLiquidity() internal {
```

#### Line 263 (L255–L271)
```solidity
    255:         IERC20(matic).safeTransfer(strategist, strategistFee);
    256: 
    257:     }
    258: 
    259: 
    260: 
    261:     // Adds liquidity to AMM and gets more LP tokens.
    262: 
>>  263:     function addLiquidity() internal {
    264: 
    265:         uint256 outputHalf = IERC20(output).balanceOf(address(this)).div(2);
    266: 
    267: 
    268: 
    269:         if (lpToken0 != output) {
    270: 
    271:             IUniswapRouterETH(unirouter).swapExactTokensForTokens(outputHalf, 0, outputToLp0Route, address(this), now);
```

#### Line 265 (L257–L273)
```solidity
    257:     }
    258: 
    259: 
    260: 
    261:     // Adds liquidity to AMM and gets more LP tokens.
    262: 
    263:     function addLiquidity() internal {
    264: 
>>  265:         uint256 outputHalf = IERC20(output).balanceOf(address(this)).div(2);
    266: 
    267: 
    268: 
    269:         if (lpToken0 != output) {
    270: 
    271:             IUniswapRouterETH(unirouter).swapExactTokensForTokens(outputHalf, 0, outputToLp0Route, address(this), now);
    272: 
    273:         }
```

#### Line 271 (L263–L279)
```solidity
    263:     function addLiquidity() internal {
    264: 
    265:         uint256 outputHalf = IERC20(output).balanceOf(address(this)).div(2);
    266: 
    267: 
    268: 
    269:         if (lpToken0 != output) {
    270: 
>>  271:             IUniswapRouterETH(unirouter).swapExactTokensForTokens(outputHalf, 0, outputToLp0Route, address(this), now);
    272: 
    273:         }
    274: 
    275: 
    276: 
    277:         if (lpToken1 != output) {
    278: 
    279:             IUniswapRouterETH(unirouter).swapExactTokensForTokens(outputHalf, 0, outputToLp1Route, address(this), now);
```

#### Line 279 (L271–L287)
```solidity
    271:             IUniswapRouterETH(unirouter).swapExactTokensForTokens(outputHalf, 0, outputToLp0Route, address(this), now);
    272: 
    273:         }
    274: 
    275: 
    276: 
    277:         if (lpToken1 != output) {
    278: 
>>  279:             IUniswapRouterETH(unirouter).swapExactTokensForTokens(outputHalf, 0, outputToLp1Route, address(this), now);
    280: 
    281:         }
    282: 
    283: 
    284: 
    285:         uint256 lp0Bal = IERC20(lpToken0).balanceOf(address(this));
    286: 
    287:         uint256 lp1Bal = IERC20(lpToken1).balanceOf(address(this));
```

#### Line 285 (L277–L293)
```solidity
    277:         if (lpToken1 != output) {
    278: 
    279:             IUniswapRouterETH(unirouter).swapExactTokensForTokens(outputHalf, 0, outputToLp1Route, address(this), now);
    280: 
    281:         }
    282: 
    283: 
    284: 
>>  285:         uint256 lp0Bal = IERC20(lpToken0).balanceOf(address(this));
    286: 
    287:         uint256 lp1Bal = IERC20(lpToken1).balanceOf(address(this));
    288: 
    289:         IUniswapRouterETH(unirouter).addLiquidity(lpToken0, lpToken1, lp0Bal, lp1Bal, 1, 1, address(this), now);
    290: 
    291:     }
    292: 
    293: 
```

#### Line 287 (L279–L295)
```solidity
    279:             IUniswapRouterETH(unirouter).swapExactTokensForTokens(outputHalf, 0, outputToLp1Route, address(this), now);
    280: 
    281:         }
    282: 
    283: 
    284: 
    285:         uint256 lp0Bal = IERC20(lpToken0).balanceOf(address(this));
    286: 
>>  287:         uint256 lp1Bal = IERC20(lpToken1).balanceOf(address(this));
    288: 
    289:         IUniswapRouterETH(unirouter).addLiquidity(lpToken0, lpToken1, lp0Bal, lp1Bal, 1, 1, address(this), now);
    290: 
    291:     }
    292: 
    293: 
    294: 
    295:     // calculate the total underlaying 'want' held by the strat.
```

#### Line 289 (L281–L297)
```solidity
    281:         }
    282: 
    283: 
    284: 
    285:         uint256 lp0Bal = IERC20(lpToken0).balanceOf(address(this));
    286: 
    287:         uint256 lp1Bal = IERC20(lpToken1).balanceOf(address(this));
    288: 
>>  289:         IUniswapRouterETH(unirouter).addLiquidity(lpToken0, lpToken1, lp0Bal, lp1Bal, 1, 1, address(this), now);
    290: 
    291:     }
    292: 
    293: 
    294: 
    295:     // calculate the total underlaying 'want' held by the strat.
    296: 
    297:     function balanceOf() public view returns (uint256) {
```

#### Line 297 (L289–L305)
```solidity
    289:         IUniswapRouterETH(unirouter).addLiquidity(lpToken0, lpToken1, lp0Bal, lp1Bal, 1, 1, address(this), now);
    290: 
    291:     }
    292: 
    293: 
    294: 
    295:     // calculate the total underlaying 'want' held by the strat.
    296: 
>>  297:     function balanceOf() public view returns (uint256) {
    298: 
    299:         return balanceOfWant().add(balanceOfPool());
    300: 
    301:     }
    302: 
    303: 
    304: 
    305:     // it calculates how much 'want' this contract holds.
```

#### Line 309 (L301–L317)
```solidity
    301:     }
    302: 
    303: 
    304: 
    305:     // it calculates how much 'want' this contract holds.
    306: 
    307:     function balanceOfWant() public view returns (uint256) {
    308: 
>>  309:         return IERC20(want).balanceOf(address(this));
    310: 
    311:     }
    312: 
    313: 
    314: 
    315:     // it calculates how much 'want' the strategy has working in the farm.
    316: 
    317:     function balanceOfPool() public view returns (uint256) {
```

#### Line 319 (L311–L327)
```solidity
    311:     }
    312: 
    313: 
    314: 
    315:     // it calculates how much 'want' the strategy has working in the farm.
    316: 
    317:     function balanceOfPool() public view returns (uint256) {
    318: 
>>  319:         return IRewardPool(rewardPool).balanceOf(address(this));
    320: 
    321:     }
    322: 
    323: 
    324: 
    325:     // called as part of strat migration. Sends all the available funds back to the vault.
    326: 
    327:     function retireStrat() external {
```

#### Line 337 (L329–L345)
```solidity
    329:         require(msg.sender == vault, "!vault");
    330: 
    331: 
    332: 
    333:         IRewardPool(rewardPool).withdraw(balanceOfPool());
    334: 
    335: 
    336: 
>>  337:         uint256 wantBal = IERC20(want).balanceOf(address(this));
    338: 
    339:         IERC20(want).transfer(vault, wantBal);
    340: 
    341:     }
    342: 
    343: 
    344: 
    345:     // pauses deposits and withdraws all funds from third party systems.
```

#### Line 387 (L379–L395)
```solidity
    379:         deposit();
    380: 
    381:     }
    382: 
    383: 
    384: 
    385:     function _giveAllowances() internal {
    386: 
>>  387:         IERC20(want).safeApprove(rewardPool, uint256(-1));
    388: 
    389:         IERC20(output).safeApprove(unirouter, uint256(-1));
    390: 
    391: 
    392: 
    393:         IERC20(lpToken0).safeApprove(unirouter, 0);
    394: 
    395:         IERC20(lpToken0).safeApprove(unirouter, uint256(-1));
```

#### Line 389 (L381–L397)
```solidity
    381:     }
    382: 
    383: 
    384: 
    385:     function _giveAllowances() internal {
    386: 
    387:         IERC20(want).safeApprove(rewardPool, uint256(-1));
    388: 
>>  389:         IERC20(output).safeApprove(unirouter, uint256(-1));
    390: 
    391: 
    392: 
    393:         IERC20(lpToken0).safeApprove(unirouter, 0);
    394: 
    395:         IERC20(lpToken0).safeApprove(unirouter, uint256(-1));
    396: 
    397: 
```

#### Line 393 (L385–L401)
```solidity
    385:     function _giveAllowances() internal {
    386: 
    387:         IERC20(want).safeApprove(rewardPool, uint256(-1));
    388: 
    389:         IERC20(output).safeApprove(unirouter, uint256(-1));
    390: 
    391: 
    392: 
>>  393:         IERC20(lpToken0).safeApprove(unirouter, 0);
    394: 
    395:         IERC20(lpToken0).safeApprove(unirouter, uint256(-1));
    396: 
    397: 
    398: 
    399:         IERC20(lpToken1).safeApprove(unirouter, 0);
    400: 
    401:         IERC20(lpToken1).safeApprove(unirouter, uint256(-1));
```

#### Line 395 (L387–L403)
```solidity
    387:         IERC20(want).safeApprove(rewardPool, uint256(-1));
    388: 
    389:         IERC20(output).safeApprove(unirouter, uint256(-1));
    390: 
    391: 
    392: 
    393:         IERC20(lpToken0).safeApprove(unirouter, 0);
    394: 
>>  395:         IERC20(lpToken0).safeApprove(unirouter, uint256(-1));
    396: 
    397: 
    398: 
    399:         IERC20(lpToken1).safeApprove(unirouter, 0);
    400: 
    401:         IERC20(lpToken1).safeApprove(unirouter, uint256(-1));
    402: 
    403:     }
```

#### Line 399 (L391–L407)
```solidity
    391: 
    392: 
    393:         IERC20(lpToken0).safeApprove(unirouter, 0);
    394: 
    395:         IERC20(lpToken0).safeApprove(unirouter, uint256(-1));
    396: 
    397: 
    398: 
>>  399:         IERC20(lpToken1).safeApprove(unirouter, 0);
    400: 
    401:         IERC20(lpToken1).safeApprove(unirouter, uint256(-1));
    402: 
    403:     }
    404: 
    405: 
    406: 
    407:     function _removeAllowances() internal {
```

#### Line 401 (L393–L409)
```solidity
    393:         IERC20(lpToken0).safeApprove(unirouter, 0);
    394: 
    395:         IERC20(lpToken0).safeApprove(unirouter, uint256(-1));
    396: 
    397: 
    398: 
    399:         IERC20(lpToken1).safeApprove(unirouter, 0);
    400: 
>>  401:         IERC20(lpToken1).safeApprove(unirouter, uint256(-1));
    402: 
    403:     }
    404: 
    405: 
    406: 
    407:     function _removeAllowances() internal {
    408: 
    409:         IERC20(want).safeApprove(rewardPool, 0);
```

#### Line 409 (L401–L417)
```solidity
    401:         IERC20(lpToken1).safeApprove(unirouter, uint256(-1));
    402: 
    403:     }
    404: 
    405: 
    406: 
    407:     function _removeAllowances() internal {
    408: 
>>  409:         IERC20(want).safeApprove(rewardPool, 0);
    410: 
    411:         IERC20(output).safeApprove(unirouter, 0);
    412: 
    413:         IERC20(lpToken0).safeApprove(unirouter, 0);
    414: 
    415:         IERC20(lpToken1).safeApprove(unirouter, 0);
    416: 
    417:     }
```

#### Line 411 (L403–L419)
```solidity
    403:     }
    404: 
    405: 
    406: 
    407:     function _removeAllowances() internal {
    408: 
    409:         IERC20(want).safeApprove(rewardPool, 0);
    410: 
>>  411:         IERC20(output).safeApprove(unirouter, 0);
    412: 
    413:         IERC20(lpToken0).safeApprove(unirouter, 0);
    414: 
    415:         IERC20(lpToken1).safeApprove(unirouter, 0);
    416: 
    417:     }
    418: 
    419: }
```

#### Line 413 (L405–L420)
```solidity
    405: 
    406: 
    407:     function _removeAllowances() internal {
    408: 
    409:         IERC20(want).safeApprove(rewardPool, 0);
    410: 
    411:         IERC20(output).safeApprove(unirouter, 0);
    412: 
>>  413:         IERC20(lpToken0).safeApprove(unirouter, 0);
    414: 
    415:         IERC20(lpToken1).safeApprove(unirouter, 0);
    416: 
    417:     }
    418: 
    419: }
    420: 
```

#### Line 415 (L407–L420)
```solidity
    407:     function _removeAllowances() internal {
    408: 
    409:         IERC20(want).safeApprove(rewardPool, 0);
    410: 
    411:         IERC20(output).safeApprove(unirouter, 0);
    412: 
    413:         IERC20(lpToken0).safeApprove(unirouter, 0);
    414: 
>>  415:         IERC20(lpToken1).safeApprove(unirouter, 0);
    416: 
    417:     }
    418: 
    419: }
    420: 
```

## `contracts/archive/vaults/BeefyVaultV6.sol` (203 lines)
### Functions / Constructors
- L47: `constructor` — `constructor (         IStrategy _strategy,         string memory _name,         string memory _symbol,         uint256 _approvalDelay`
- L60: `want` — `function want() public view returns (IERC20) {         return IERC20(strategy.want());     }      /**`
- L69: `balance` — `function balance() public view returns (uint) {         return want().balanceOf(address(this)).add(IStrategy(strategy).balanceOf());     }      /**`
- L79: `available` — `function available() public view returns (uint256) {         return want().balanceOf(address(this));     }      /**`
- L87: `getPricePerFullShare` — `function getPricePerFullShare() public view returns (uint256) {         return totalSupply() == 0 ? 1e18 : balance().mul(1e18).div(totalSupply());     }      /*`
- L94: `depositAll` — `function depositAll() external {         deposit(want().balanceOf(msg.sender));     }      /**`
- L102: `deposit` — `function deposit(uint _amount) public nonReentrant {         strategy.beforeDeposit();          uint256 _pool = balance();         want().safeTransferFrom(msg.s`
- L123: `earn` — `function earn() public {         uint _bal = available();         want().safeTransfer(address(strategy), _bal);         strategy.deposit();     }`
- L132: `withdrawAll` — `function withdrawAll() external {         withdraw(balanceOf(msg.sender));     }      /**`
- L141: `withdraw` — `function withdraw(uint256 _shares) public {         uint256 r = (balance().mul(_shares)).div(totalSupply());         _burn(msg.sender, _shares);          uint b`
- L163: `proposeStrat` — `function proposeStrat(address _implementation) public onlyOwner {         require(address(this) == IStrategy(_implementation).vault(), "Proposal not valid for t`
- L179: `upgradeStrat` — `function upgradeStrat() public onlyOwner {         require(stratCandidate.implementation != address(0), "There is no candidate");         require(stratCandidate`
- L197: `inCaseTokensGetStuck` — `function inCaseTokensGetStuck(address _token) external onlyOwner {         require(_token != address(want()), "!token");          uint256 amount = IERC20(_token`

### Sink Windows (±8 lines)
#### Line 70 (L62–L78)
```solidity
     62:     }
     63: 
     64:     /**
     65:      * @dev It calculates the total underlying value of {token} held by the system.
     66:      * It takes into account the vault contract balance, the strategy contract balance
     67:      *  and the balance deployed in other contracts as part of the strategy.
     68:      */
     69:     function balance() public view returns (uint) {
>>   70:         return want().balanceOf(address(this)).add(IStrategy(strategy).balanceOf());
     71:     }
     72: 
     73:     /**
     74:      * @dev Custom logic in here for how much the vault allows to be borrowed.
     75:      * We return 100% of tokens for now. Under certain conditions we might
     76:      * want to keep some of the system funds at hand in the vault, instead
     77:      * of putting them to work.
     78:      */
```

#### Line 80 (L72–L88)
```solidity
     72: 
     73:     /**
     74:      * @dev Custom logic in here for how much the vault allows to be borrowed.
     75:      * We return 100% of tokens for now. Under certain conditions we might
     76:      * want to keep some of the system funds at hand in the vault, instead
     77:      * of putting them to work.
     78:      */
     79:     function available() public view returns (uint256) {
>>   80:         return want().balanceOf(address(this));
     81:     }
     82: 
     83:     /**
     84:      * @dev Function for various UIs to display the current value of one of our yield tokens.
     85:      * Returns an uint256 with 18 decimals of how much underlying asset one vault share represents.
     86:      */
     87:     function getPricePerFullShare() public view returns (uint256) {
     88:         return totalSupply() == 0 ? 1e18 : balance().mul(1e18).div(totalSupply());
```

#### Line 95 (L87–L103)
```solidity
     87:     function getPricePerFullShare() public view returns (uint256) {
     88:         return totalSupply() == 0 ? 1e18 : balance().mul(1e18).div(totalSupply());
     89:     }
     90: 
     91:     /**
     92:      * @dev A helper function to call deposit() with all the sender's funds.
     93:      */
     94:     function depositAll() external {
>>   95:         deposit(want().balanceOf(msg.sender));
     96:     }
     97: 
     98:     /**
     99:      * @dev The entrypoint of funds into the system. People deposit with this function
    100:      * into the vault. The vault is then in charge of sending funds into the strategy.
    101:      */
    102:     function deposit(uint _amount) public nonReentrant {
    103:         strategy.beforeDeposit();
```

#### Line 106 (L98–L114)
```solidity
     98:     /**
     99:      * @dev The entrypoint of funds into the system. People deposit with this function
    100:      * into the vault. The vault is then in charge of sending funds into the strategy.
    101:      */
    102:     function deposit(uint _amount) public nonReentrant {
    103:         strategy.beforeDeposit();
    104: 
    105:         uint256 _pool = balance();
>>  106:         want().safeTransferFrom(msg.sender, address(this), _amount);
    107:         earn();
    108:         uint256 _after = balance();
    109:         _amount = _after.sub(_pool); // Additional check for deflationary tokens
    110:         uint256 shares = 0;
    111:         if (totalSupply() == 0) {
    112:             shares = _amount;
    113:         } else {
    114:             shares = (_amount.mul(totalSupply())).div(_pool);
```

#### Line 125 (L117–L133)
```solidity
    117:     }
    118: 
    119:     /**
    120:      * @dev Function to send funds into the strategy and put them to work. It's primarily called
    121:      * by the vault's deposit() function.
    122:      */
    123:     function earn() public {
    124:         uint _bal = available();
>>  125:         want().safeTransfer(address(strategy), _bal);
    126:         strategy.deposit();
    127:     }
    128: 
    129:     /**
    130:      * @dev A helper function to call withdraw() with all the sender's funds.
    131:      */
    132:     function withdrawAll() external {
    133:         withdraw(balanceOf(msg.sender));
```

#### Line 133 (L125–L141)
```solidity
    125:         want().safeTransfer(address(strategy), _bal);
    126:         strategy.deposit();
    127:     }
    128: 
    129:     /**
    130:      * @dev A helper function to call withdraw() with all the sender's funds.
    131:      */
    132:     function withdrawAll() external {
>>  133:         withdraw(balanceOf(msg.sender));
    134:     }
    135: 
    136:     /**
    137:      * @dev Function to exit the system. The vault will withdraw the required tokens
    138:      * from the strategy and pay up the token holder. A proportional number of IOU
    139:      * tokens are burned in the process.
    140:      */
    141:     function withdraw(uint256 _shares) public {
```

#### Line 145 (L137–L153)
```solidity
    137:      * @dev Function to exit the system. The vault will withdraw the required tokens
    138:      * from the strategy and pay up the token holder. A proportional number of IOU
    139:      * tokens are burned in the process.
    140:      */
    141:     function withdraw(uint256 _shares) public {
    142:         uint256 r = (balance().mul(_shares)).div(totalSupply());
    143:         _burn(msg.sender, _shares);
    144: 
>>  145:         uint b = want().balanceOf(address(this));
    146:         if (b < r) {
    147:             uint _withdraw = r.sub(b);
    148:             strategy.withdraw(_withdraw);
    149:             uint _after = want().balanceOf(address(this));
    150:             uint _diff = _after.sub(b);
    151:             if (_diff < _withdraw) {
    152:                 r = b.add(_diff);
    153:             }
```

#### Line 149 (L141–L157)
```solidity
    141:     function withdraw(uint256 _shares) public {
    142:         uint256 r = (balance().mul(_shares)).div(totalSupply());
    143:         _burn(msg.sender, _shares);
    144: 
    145:         uint b = want().balanceOf(address(this));
    146:         if (b < r) {
    147:             uint _withdraw = r.sub(b);
    148:             strategy.withdraw(_withdraw);
>>  149:             uint _after = want().balanceOf(address(this));
    150:             uint _diff = _after.sub(b);
    151:             if (_diff < _withdraw) {
    152:                 r = b.add(_diff);
    153:             }
    154:         }
    155: 
    156:         want().safeTransfer(msg.sender, r);
    157:     }
```

#### Line 156 (L148–L164)
```solidity
    148:             strategy.withdraw(_withdraw);
    149:             uint _after = want().balanceOf(address(this));
    150:             uint _diff = _after.sub(b);
    151:             if (_diff < _withdraw) {
    152:                 r = b.add(_diff);
    153:             }
    154:         }
    155: 
>>  156:         want().safeTransfer(msg.sender, r);
    157:     }
    158: 
    159:     /** 
    160:      * @dev Sets the candidate for the new strat to use with this vault.
    161:      * @param _implementation The address of the candidate strategy.  
    162:      */
    163:     function proposeStrat(address _implementation) public onlyOwner {
    164:         require(address(this) == IStrategy(_implementation).vault(), "Proposal not valid for this Vault");
```

#### Line 200 (L192–L203)
```solidity
    192: 
    193:     /**
    194:      * @dev Rescues random funds stuck that the strat can't handle.
    195:      * @param _token address of the token to rescue.
    196:      */
    197:     function inCaseTokensGetStuck(address _token) external onlyOwner {
    198:         require(_token != address(want()), "!token");
    199: 
>>  200:         uint256 amount = IERC20(_token).balanceOf(address(this));
    201:         IERC20(_token).safeTransfer(msg.sender, amount);
    202:     }
    203: }
```

#### Line 201 (L193–L203)
```solidity
    193:     /**
    194:      * @dev Rescues random funds stuck that the strat can't handle.
    195:      * @param _token address of the token to rescue.
    196:      */
    197:     function inCaseTokensGetStuck(address _token) external onlyOwner {
    198:         require(_token != address(want()), "!token");
    199: 
    200:         uint256 amount = IERC20(_token).balanceOf(address(this));
>>  201:         IERC20(_token).safeTransfer(msg.sender, amount);
    202:     }
    203: }
```
