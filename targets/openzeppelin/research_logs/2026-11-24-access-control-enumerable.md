# AccessControlEnumerable 역할 목록 검토

공식 범위에서 TimelockController 운영 배포의 체인·주소가 여전히 확인되지 않아, 같은 고정 릴리스의 AccessControlEnumerable을 검토했다. 검토 대상은 역할의 권한 상태와 목록의 일치 여부다. [공식 범위](https://immunefi.com/bug-bounty/openzeppelin/scope/) · [고정 소스](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/cab19933c33c2ad1d4c7a84864a3601dddfd16f3/contracts/access/extensions/AccessControlEnumerable.sol)

| 검토 항목 | 기대값과 관찰값 |
| --- | --- |
| 역할 부여·회수 | 상위 권한 상태가 실제로 바뀔 때 목록을 갱신한다. 기존 테스트에서 세 계정에 역할을 부여하고 한 계정에서 회수한 뒤 수·인덱스 조회·전체 목록이 기대한 두 계정과 일치했다. |
| 역할 포기 | 포기한 계정이 목록에서 빠져야 한다. 기존 테스트에서 보유자 수가 0 → 1 → 0으로 바뀌었다. |
| 목록을 읽는 호출자 | 문서는 목록 순서를 보장하지 않으며, 여러 번 조회할 때 같은 블록을 사용하도록 안내한다. 전체 목록 복사 비용은 크기에 비례해 늘어날 수 있다. 이번 확인은 코드와 문서에 근거한다. |

원본 Hardhat 테스트 **37개 통과**. 확인된 취약점은 없다. 특정 통합 계약의 조회 방식과 대규모 목록의 가스 비용은 검증 범위에 포함되지 않았다. 운영 배포 검토는 공식 범위와 연결되는 체인·주소가 필요하다. [실행 로그](../evidence/access-control-enumerable-test.log) · [집계 데이터](2026-11-24-access-control-enumerable.json)
