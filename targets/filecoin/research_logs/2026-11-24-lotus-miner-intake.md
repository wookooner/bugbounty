# Filecoin Lotus miner 첫 검토

공식 범위에 개별 등록된 Lotus miner를 첫 대상으로 선택했다. 안정 릴리스 v1.39.1에서 `miner/`의 세 Go 파일과 버전 확인용 `go.mod`, 라이선스를 로컬에 확보했다. [범위](https://immunefi.com/bug-bounty/filecoin/scope/) · [릴리스](https://github.com/filecoin-project/lotus/releases/tag/v1.39.1)

| 확인 항목 | 관찰 |
| --- | --- |
| 체인 입력 | `GetBestMiningCandidate`는 FullNode의 `ChainHead` 응답을 읽고 헤드가 바뀌면 채굴 기준을 갱신한다. |
| 블록 생성 | `mineOne`은 라운드 기준 정보를 받아 메시지를 선택한다. 블록 템플릿은 FullNode의 `MinerCreateBlock`으로 전달된다. |
| 결과 전달 | 채굴 루프는 생성된 블록을 `SyncSubmitBlock`으로 넘긴다. |

이번 세션은 소스 읽기와 환경 사전 확인을 수행했다. Docker CLI의 존재를 확인했고 Go 컴파일러, devnet 기동, 테스트 결과는 아직 확인하지 않았다. 확인된 취약점은 없다. [고정 소스](https://github.com/filecoin-project/lotus/blob/6a8b57bf415c298b8908013df3ef3ea1a1a977dc/miner/miner.go) · [집계용 JSON](2026-11-24-lotus-miner-intake.json)

**다음 단계**

공식 Audit Kit가 사용하는 Lotus 버전과 로컬 실행 요건을 확인한다. 고정 릴리스와 호환되는 경우 격리된 devnet에서 정상 기동과 체인 높이 증가를 검증한다.
