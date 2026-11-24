# OpenZeppelin Contracts 검토 범위

- 대상은 OpenZeppelin Contracts v5.7.0의 커밋 `cab19933c33c2ad1d4c7a84864a3601dddfd16f3`이다. [원본 소스](https://github.com/OpenZeppelin/openzeppelin-contracts/tree/cab19933c33c2ad1d4c7a84864a3601dddfd16f3)
- 현재 검토 모듈은 `AccessControl`, `AccessControlDefaultAdminRules`, `TimelockController`다. 테스트 및 형식 검증용 파일은 동작 근거로 참조했다. [공식 범위](https://immunefi.com/bug-bounty/openzeppelin/scope/) · [프로그램 자료](https://immunefi.com/bug-bounty/openzeppelin/resources/)
- 검증은 고정된 소스와 독립 로컬 Hardhat 환경을 사용했다. 확인한 운영 배포 주소는 없다.
