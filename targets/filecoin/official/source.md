# Filecoin 소스 기준

확인일 2026-11-24. Lotus v1.39.1 태그를 커밋 `6a8b57bf415c298b8908013df3ef3ea1a1a977dc`에 고정했다. [릴리스](https://github.com/filecoin-project/lotus/releases/tag/v1.39.1) · [고정 miner 소스](https://github.com/filecoin-project/lotus/tree/6a8b57bf415c298b8908013df3ef3ea1a1a977dc/miner)

첫 검토 입력은 `miner/miner.go`, `miner/testminer.go`, `miner/warmup.go`다. `go.mod`와 라이선스를 함께 확보했다. 전체 노드 실행이나 Audit Kit 호환성은 별도 확인한다.
