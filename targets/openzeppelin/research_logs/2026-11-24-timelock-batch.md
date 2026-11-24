# TimelockController 배치 실행 검토

OpenZeppelin Contracts v5.7.0의 고정 커밋에서 수행했다. Immunefi 자료로 라이브러리 자산과 영향 기준을 재확인했다. mocks는 로컬 테스트 증거로 사용했다. [프로그램 범위](https://immunefi.com/bug-bounty/openzeppelin/scope/) · [자료](https://immunefi.com/bug-bounty/openzeppelin/resources/)

| 검토 항목 | 관찰 결과 |
| --- | --- |
| 공개 배치와 예약 시각 | 역할 없는 실행자가 공개 설정에서 예약 시각과 같은 블록에 두 호출을 실행했다. 실행 이벤트 2건, Done, 수신 잔액 1 wei를 확인했다. |
| 예약 취소 | 취소 이벤트가 발생하고 배치 예약 시각이 0으로 초기화됐다. |
| 배치 도중 대상 호출 실패 | 거래가 되돌아갔다. 예약은 Ready로 남았고 두 계약 잔액은 0 wei였다. 실행 및 수신 이벤트도 남지 않았다. |
| 지정 실행과 시간 제한 | 선택한 원본 테스트에서 준비 전 실행과 권한 없는 실행은 거부됐다. |

로컬 추가 테스트 3개와 선택 원본 테스트 10개가 통과했다. 원본 선택에는 앞선 세션에서 실행한 테스트가 일부 포함된다. [추가 테스트](../evidence/checks/timelock-batch-behavior.test.js) · [추가 로그](../evidence/timelock-batch-behavior.log) · [원본 로그](../evidence/timelock-batch-upstream.log) · [집계 데이터](2026-11-24-timelock-batch.json)

**공개 자료 대조.** v5.0 감사 L-16에 예약 시각을 포함하는 동작이 이미 기술돼 있다. v4.4.0 형식검증 보고서는 역사적 참고 자료로 확인했다. GHSA-fg47-3c2x-m2wr의 영향 버전에 v5.7.0은 포함되지 않는다. 이번 검토에서 확인된 취약점은 없고 심각도는 산정하지 않았다. [v5.0 감사](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.7.0/audits/2023-10-v5.0.pdf) · [형식검증](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.7.0/fv/reports/2022-03.pdf) · [공개 권고](https://github.com/OpenZeppelin/openzeppelin-contracts/security/advisories/GHSA-fg47-3c2x-m2wr)

정해진 소스 검토 범위는 마무리했다. 운영 권한과 실제 영향 검토에는 공식 범위에서 확인한 체인과 배포 주소가 필요하다.
