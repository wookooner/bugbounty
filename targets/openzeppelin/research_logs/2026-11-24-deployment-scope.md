# TimelockController 운영 배포 식별

2026-11-24에 [Immunefi Scope](https://immunefi.com/bug-bounty/openzeppelin/scope/)의 자산 표에 있는 여섯 링크와 [공식 거버넌스 문서](https://docs.openzeppelin.com/contracts/5.x/api/governance)를 대조했다. 자산 표의 링크는 모두 GitHub 소스 또는 릴리스였다. 거버넌스 문서는 TimelockController의 사용 예를 설명하고, 이번 범위에서 검토할 체인과 주소는 식별되지 않았다.

**상태**는 배포 식별 대기다. 제3자 서비스의 주소를 연구 대상으로 추가하거나 RPC를 호출하지 않았다. 공식 범위와 연결되는 체인·주소가 확인되면 기준 블록을 고정하고, 초기 관리자와 현재 역할, 실행 설정, 최소 지연을 읽기 전용으로 확인한다. 이번 단계에서 확인된 취약점은 없다.
