# OpenZeppelin 공식 범위 확인 기록

확인일 2026-11-24. [Immunefi Scope](https://immunefi.com/bug-bounty/openzeppelin/scope/) · [Immunefi Resources](https://immunefi.com/bug-bounty/openzeppelin/resources/)

| 공식 목록 자산 | 공식 범위에 표시된 고정 조건 |
| --- | --- |
| [OpenZeppelin Contracts](https://github.com/OpenZeppelin/openzeppelin-contracts) | 이 연구는 별도로 v5.7.0의 커밋을 고정했다. |
| [OpenZeppelin Contracts Upgradeable](https://github.com/OpenZeppelin/openzeppelin-contracts-upgradeable) | 별도 저장소 |
| [Uniswap Hooks](https://github.com/OpenZeppelin/uniswap-hooks) | 별도 저장소 |
| [Confidential Contracts](https://github.com/OpenZeppelin/openzeppelin-confidential-contracts/releases/tag/v0.5.3) | v0.5.3, `4a4f6c71f58b75e391899b57e42e3b73d288dfe3`. mocks와 examples 제외 |
| Axelar Gateway Adapter 및 ERC7786OpenBridge | 두 자산 모두 `0361935dc5edd233adbb9fbae5871ccbb8c739d8`만 해당 |

Contracts 자료는 `contracts/`에서 `mocks/`와 `vendor/`를 제외한다고 명시한다. 영향은 공식 표를 따른다. 이 표의 자산 링크는 GitHub 저장소, 릴리스 또는 Solidity 파일을 가리킨다. TimelockController의 운영 체인과 주소는 지정하지 않는다.
