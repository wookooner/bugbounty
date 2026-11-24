# Filecoin 공식 범위 확인 기록

확인일 2026-11-24. [Immunefi Scope](https://immunefi.com/bug-bounty/filecoin/scope/)

- 자산 목록은 Lotus miner, Boost, go-graphsync, cbor-gen, Filecoin Proofs 계열과 여러 암호 라이브러리를 개별 열거한다. 이번 연구의 첫 대상은 공식 링크가 가리키는 [Lotus miner](https://github.com/filecoin-project/lotus/tree/master/miner)다.
- 단위 테스트, 정적 분석, 퍼저 출력만으로는 제출 요건을 충족하지 않는다. 공식 범위는 Audit Kit 기반 로컬 devnet에서의 동작과 영향 증거를 요구한다.
- 연구 실행은 격리된 로컬 환경으로 제한한다. 영향과 심각도는 프로그램의 공식 표를 확인한다.
