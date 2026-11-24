# AccessManager 역할 활성화와 실행 지연

OpenZeppelin Contracts v5.7.0의 고정 커밋에서 역할 활성화와 일반 함수의 권한 판정을 검토했다. 독립 로컬 Hardhat에서 원본 선택 테스트 **25개가 통과**했다. [공식 범위](https://immunefi.com/bug-bounty/openzeppelin/scope/) · [고정 소스](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/cab19933c33c2ad1d4c7a84864a3601dddfd16f3/contracts/access/manager/AccessManager.sol)

| 확인 항목 | 관찰 결과 |
| --- | --- |
| 역할 활성화 | 새 역할의 활성화 시각은 부여 시각에 부여 지연을 더한 값이다. `hasRole`의 보유 여부는 활성화 이전에 거짓이고, 활성화 시각에 참이 된다. 보유 여부와 함께 반환하는 실행 지연은 활성화 전에 이미 설정되어 있을 수 있다. |
| 일반 함수의 권한 판정 | `canCall`은 활성 역할이 없으면 `(false, 0)`, 활성 역할과 실행 지연이 없으면 `(true, 0)`, 활성 역할과 실행 지연이 있으면 `(false, delay)`를 반환한다. |

이번 테스트는 조회값과 권한 판정에 한정했다. 예약 작업의 실제 실행과 소비, `setAuthority` 전용 분기, 운영 배포는 확인하지 않았다. 확인된 취약점은 없다. [집계용 JSON](2026-11-24-access-manager-role-timing.json) · [실행 로그](../evidence/access-manager-role-timing.log)

**다음 단계**는 AccessManaged의 restricted 경로에서 즉시 허용과 지연된 정상 작업의 예약·소비 동작을 기존 로컬 테스트로 확인하는 것이다.
