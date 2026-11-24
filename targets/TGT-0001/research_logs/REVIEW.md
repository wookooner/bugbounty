# OpenZeppelin Contracts v5.7.0 검토 기록

- 기준 커밋 `cab19933c33c2ad1d4c7a84864a3601dddfd16f3`
- 검토 목적은 `AccessControl`의 기본 권한 모델과 테스트 기대 동작 확인이다.
- [공식 범위](https://immunefi.com/bug-bounty/openzeppelin/scope/)와 [프로그램 자료](https://immunefi.com/bug-bounty/openzeppelin/resources/)를 참조했다.
- `AccessControl.sol`의 `grantRole`과 `revokeRole`은 해당 역할의 관리자 역할을 요구한다. `renounceRole`은 호출자 확인 주소를 검사한다. `_setRoleAdmin`은 내부 함수다.
- 구현과 전체 Solidity import 의존성, 기존 테스트 읽기용 사본, LICENSE를 내려받았다.
- 정적 읽기만 수행했다. 테스트 실행에는 원본 Hardhat 환경과 테스트용 계약이 필요하다.
- 신규 가설과 확인된 취약점은 없다. 상속 계약에서 초기 관리자 역할을 어떤 방식으로 설정하는지는 후속 검토 항목이다.

## 2026-11-24 후속 세션

### 검토 계획

1. 고정된 릴리스에서 기본 역할과 기본 관리자 초기화 경로를 추적한다.
2. 관리자 이전·취소·포기 및 지연 변경의 호출 권한과 시각 조건을 확인한다.
3. 원본 테스트를 로컬에서 실행하고 관찰, 검증 결과, 후속 항목을 데이터로 저장한다.
4. 공식 상속 예시에서 생성자 인수와 공개 진입점을 확인한다.

초기 관리자는 `AccessControlDefaultAdminRules` 생성자에서 지정하며 0 주소는 거부한다. 기존 관리자만 이전을 예약·취소할 수 있고, 새 관리자는 지정된 시각을 초과한 뒤 수락한다. 역할 포기에는 0 주소로의 예약과 지연 경과가 필요하다. 기존 테스트에서 예약 시각과 정확히 같은 경우도 검증했다.

두 원본 테스트 파일을 로컬 Hardhat 환경에서 실행해 **144개가 통과**했다. 위쪽 세션의 실행 미확인 상태는 이 결과로 갱신됐다. 확인된 취약점과 신규 가설은 없다. 공식 MyToken 상속 예시는 배포 호출자를 최초 관리자로 지정하고 3일 지연을 설정한다. 실제 상속 계약의 배포 설정과 공개 진입점은 검토 대상으로 지정되면 확인한다.

집계용 [세션 데이터](2026-11-24-access-control.json)는 대상 커밋, 검사별 ID와 코드 줄, 검증 방법과 결과, 확인된 취약점 목록, 후속 작업을 담는다. 코드의 원본 경로는 JSON의 `target.commit` 기준이다.

원본 프로젝트와 같은 Solidity 0.8.35 및 Osaka 설정을 쓰는 최소 로컬 Hardhat 환경으로 실행했다. 아래 명령은 이 폴더에서 실행한다.

```sh
XDG_CONFIG_HOME="$PWD/.hardhat/config" \
XDG_CACHE_HOME="$PWD/.hardhat/cache" \
XDG_DATA_HOME="$PWD/.hardhat/data" \
HARDHAT_DISABLE_TELEMETRY=1 \
./node_modules/.bin/hardhat test test/access/AccessControl.test.js \
  test/access/extensions/AccessControlDefaultAdminRules.test.js
```

## 2026-11-24 상속과 초기 관리자 후속 검토

- 고정 커밋의 Solidity 소스를 검색했다. `contracts/`에 `AccessControlDefaultAdminRules`의 구체 상속 계약은 발견되지 않았다. `fv/`의 형식 검증용 하네스는 생성자 인수로 받은 초기 관리자 주소를 전달한다. [형식 검증 하네스](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/cab19933c33c2ad1d4c7a84864a3601dddfd16f3/fv/harnesses/AccessControlDefaultAdminRulesHarness.sol)
- 배포 가능한 `AccessControl` 직접 상속 사례인 `TimelockController`를 이어서 검토했다. 초기에는 계약 자체가 기본 관리자다. 생성자에 0이 아닌 주소를 전달한 경우 그 주소도 초기 설정용 관리자 권한을 받는다. [생성자](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/cab19933c33c2ad1d4c7a84864a3601dddfd16f3/contracts/governance/TimelockController.sol#L102-L137)
- 배포 초기 상태, 선택적 관리자, 예약·취소 권한, 최소 지연 변경 관련 원본 테스트 **9개 통과**. 이번 실행은 선택된 테스트에 한정했다. 특정 운영 배포의 관리자 주소와 역할 포기 여부는 미확인이다. 신규 가설이나 확인된 취약점은 없다.
- [집계용 세션 데이터](2026-11-24-admin-inheritance.json)에 코드 줄, 실행한 테스트 필터, 결과를 기록했다. 다음 검토 범위는 실행 권한과 작업 상태 전이다.

## 2026-11-24 실행 권한과 상태 전이

**대상과 범위.** OpenZeppelin Contracts v5.7.0의 `TimelockController` 실행 경로를 고정 커밋에서 검토했다. 테스트는 로컬 Hardhat에서 수행했다. OpenZeppelin 공식 범위와 영향 기준을 확인했다. [범위](https://immunefi.com/bug-bounty/openzeppelin/scope/)

| 확인할 규칙 | 근거와 결과 |
| --- | --- |
| 실행자는 역할 정책을 따른다 | 기존 단건·일괄 테스트에서 지정 실행자는 통과하고 기타 호출자는 거부됐다. 공개 실행 설정을 적용한 추가 단건 테스트에서는 역할 없는 호출자가 준비된 작업을 실행했고, `CallExecuted`와 `Done`을 확인했다. |
| 실행 전에 준비 상태와 선행 작업 완료가 필요하다 | 미예약 및 지연 미경과 실행은 거부됐다. 선행 작업이 완료된 뒤 실행할 수 있었다. |
| 정상 외부 호출에서 예약한 ETH 값이 전달된다 | 수신 계약 잔액은 0에서 1 wei로 바뀌었다. 실패하는 별도 케이스에서는 `FailedCall`이 발생했고 두 계약 잔액이 0으로 유지됐다. |

원본 선택 테스트 14개와 추가 동작 테스트 1개가 통과했다. 공개 실행의 배치 경로는 코드에서 확인했고 추가 테스트는 단건으로 한정했다. 특정 운영 배포의 역할 설정과 자산 규모는 미확인이다. [실행 코드](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/cab19933c33c2ad1d4c7a84864a3601dddfd16f3/contracts/governance/TimelockController.sol#L356-L435)

**중복과 영향.** 공개 권고 GHSA-fg47-3c2x-m2wr의 영향 버전에 v5.7.0은 포함되지 않는다. 프로그램 안내에서 모듈 이름을 검색했고 비공개 제출과 전체 감사 문서는 검토 범위에 포함되지 않았다. 이번 세션에서 확인된 취약점이 없어 심각도와 손실 규모는 산정하지 않았다. [공개 권고](https://github.com/OpenZeppelin/openzeppelin-contracts/security/advisories/GHSA-fg47-3c2x-m2wr) · [프로그램 안내](https://immunefi.com/bug-bounty/openzeppelin/information/)

**기록 방식.** 후속 세션에도 대상 버전과 범위, 역할·자산 흐름, 핵심 규칙, 기대와 실제 결과, 증거 위치, 알려진 이슈와 남은 항목을 남긴다. 구체적인 영향이 확인되면 전제조건과 영향 범위, 프로그램 기준에 따른 심각도 근거도 기록한다. 테스트 전문은 로그로 보관하고 보고서에는 결정에 필요한 결과를 적는다. [집계용 세션 데이터](2026-11-24-timelock-execution.json)

로컬 로그와 추가 테스트 사본은 [evidence](../evidence/)에 있다. JSON에서 원본 코드와 테스트 경로는 대상 커밋 기준이며, 로컬 증거 경로는 대상 폴더 기준이다.
