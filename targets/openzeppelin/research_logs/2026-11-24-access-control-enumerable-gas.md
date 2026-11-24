# 역할 목록 조회 비용 검토

OpenZeppelin Contracts v5.7.0의 AccessControlEnumerable에서 역할 보유자 수를 0·1·8·32명으로 늘리며 로컬 Hardhat의 `estimateGas`로 조회 비용을 측정했다. 로컬 래퍼에서 조회 결과도 검증했으며 테스트 1개가 통과했다. [고정 소스](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/cab19933c33c2ad1d4c7a84864a3601dddfd16f3/contracts/access/extensions/AccessControlEnumerable.sol#L24-L58)

| 보유자 수 | 전체 목록 | 개수 | 첫 원소 |
| ---: | ---: | ---: | ---: |
| 0 | 24,501 | 24,153 | 해당 없음 |
| 1 | 26,826 | 24,153 | 26,547 |
| 8 | 42,619 | 24,153 | 26,547 |
| 32 | 96,771 | 24,153 | 26,547 |

단위는 추정 가스다. 이 환경에서 전체 목록 조회만 표본 크기와 함께 증가했다. 수치는 로컬 래퍼와 컴파일 설정에 의존한다. 실제 통합 계약의 쓰기 경로나 운영 블록 한도는 확인하지 않았다. 이번 측정에서 확인된 취약점은 없다. [집계 데이터](2026-11-24-access-control-enumerable-gas.json) · [테스트](../evidence/checks/access-control-enumerable-gas.test.js) · [로그](../evidence/access-control-enumerable-gas.log)

**다음 단계**는 같은 고정 릴리스의 AccessManager에서 역할 활성화 시점과 권한 판정에 사용하는 실행 지연을 소스와 기존 로컬 테스트로 확인하는 것이다.
