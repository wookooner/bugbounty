전체 버그바운티 분야
연구 분야	주요 분석 대상	진입 난이도
Web Security	웹 애플리케이션, API	중
Web3 Security	스마트 컨트랙트, DeFi, 블록체인	상
Windows Security	커널, 드라이버, 시스템 서비스	최상
Linux Security	커널, 시스템 프로그램	최상
Browser Security	Chrome, Firefox, Safari	최상
Mobile Security	Android, iOS, 모바일 앱	상
Cloud Security	AWS, Azure, GCP	상
AI Security	LLM, AI 에이전트, ML 프레임워크	중~상
Binary Security	네이티브 프로그램, 라이브러리	상
Network Security	네트워크 프로토콜, 장비	상
Hardware Security	CPU, 칩셋, 임베디드 장치	최상
Supply Chain Security	패키지, 빌드, 배포 시스템	상
Virtualization Security	Hypervisor, VM, 컨테이너	최상
Cryptography	암호 알고리즘 및 구현	최상

난이도는 실질적인 취약점 발견에 필요한 사전 지식과 연구 환경을 기준으로 한 상대적인 평가다.
2. Web3 Security
블록체인의 분산 시스템, 스마트 컨트랙트, 경제적 메커니즘을 분석하는 분야다.
세부 분야	주요 연구 대상	주요 취약점
Smart Contract	Solidity, Vyper, Move, Rust	Reentrancy, Access Control, Storage Collision
DeFi	DEX, Lending, Vault, Staking	가격 조작, 회계 오류, 청산 로직 오류
Blockchain Core	Ethereum, Bitcoin, Solana 클라이언트	합의 오류, 상태 검증 오류
Layer 2	Optimistic/ZK Rollup	상태 전이 및 증명 검증 오류
Cross-chain Bridge	체인 간 자산 이동	메시지 검증, 서명 검증 오류
Cryptography	ZK Proof, MPC, 서명 알고리즘	증명 및 암호 구현 오류
Wallet	지갑, 키 관리 시스템	서명 검증, 키 관리 오류
Governance	DAO, 투표 시스템	투표권 계산 및 권한 관리 오류
MEV	트랜잭션 순서, 블록 생성	순서 의존성, 경제적 설계 결함
Web3 Infrastructure	RPC, Indexer, Oracle	데이터 검증 및 접근 제어 오류

대표적인 플랫폼
플랫폼	주요 분야
Immunefi	Web3 전문 버그바운티
Sherlock	스마트 컨트랙트 감사
Cantina	보안 감사 및 버그바운티
Code4rena	경쟁형 보안 감사 및 과거 사례
CodeHawks	경쟁형 스마트 컨트랙트 감사
Hats Finance	Web3 보안 감사 및 바운티

Immunefi에서는 스마트 컨트랙트뿐 아니라 Blockchain/DLT, 웹사이트 및 애플리케이션도 연구 범위에 포함한다. 실제 대상마다 허용 범위는 다르다. 
Immunefi+1

3. Windows Security
Windows 보안은 단순히 커널 메모리 취약점만 연구하는 분야가 아니다. 사용자 모드부터 하드웨어 가상화 계층까지 다양한 연구 대상이 존재한다.
세부 분야	주요 연구 대상	주요 취약점
Kernel	ntoskrnl, Win32k	UAF, OOB, Race Condition
Driver	WDM, WDF, 서드파티 드라이버	IOCTL 검증 오류, 메모리 안전성
System Service	Windows Services	권한 검증 오류, 권한 상승
IPC	ALPC, RPC, COM	인증 및 권한 경계 오류
File System	NTFS, ReFS	파싱 오류, 동시성 문제
Network Stack	TCP/IP, SMB, RDP	프로토콜 처리 및 메모리 오류
Authentication	LSASS, Kerberos, NTLM	인증 검증 오류
Access Control	Token, ACL, Security Descriptor	접근 제어 오류
Hypervisor	Hyper-V	가상화 격리 오류
Windows Defender	보안 엔진, 파일 파서	파싱 및 메모리 안전성
Sandbox	AppContainer, 프로세스 격리	격리 경계 오류
Virtualization-based Security	VBS, HVCI	신뢰 경계 및 보호 메커니즘 오류
Windows Applications	Office, 시스템 기본 앱	파일 파싱 및 애플리케이션 취약점
Graphics	DirectX, GPU Driver	메모리 및 객체 수명 오류

대표적인 프로그램

Microsoft MSRC Bug Bounty Programs

Microsoft는 Windows Insider Preview를 포함한 여러 제품의 버그바운티 프로그램을 운영한다. Windows Insider Preview 프로그램에는 최대 10만 달러의 보상 항목이 존재한다. 
Microsoft

4. 나머지 버그바운티 분야 세부 분류
대분류	세부 연구 분야
Web	Frontend, Backend, API, OAuth, SAML, Business Logic
Linux	Kernel, Driver, eBPF, File System, System Service
Browser	V8, SpiderMonkey, JavaScriptCore, DOM, WebAssembly, Sandbox
Mobile	Android Framework, Binder, iOS Kernel, Baseband, Mobile App
Cloud	IAM, Storage, Serverless, Multi-tenancy, Cloud Infrastructure
AI	LLM Application, Agent, RAG, Model Loading, ML Framework
Binary	File Parser, Native Application, Library, Compiler, Runtime
Network	Firewall, VPN, Router, DNS, TLS, Network Protocol
Virtualization	Hyper-V, VMware, KVM, QEMU, Docker, Kubernetes
Hardware	CPU, GPU, Firmware, UEFI, IoT, Side Channel
Supply Chain	Package Manager, CI/CD, Build System, Dependency
Cryptography	Signature, Encryption, Randomness, ZK, MPC
Automotive	ECU, CAN, Infotainment, Telematics
Enterprise	Active Directory, Exchange, ERP, SSO, Enterprise Software

브라우저 분야는 Google Chrome VRP, 모바일 및 Apple 제품은 Apple Security Bounty와 같은 전문 프로그램이 존재한다. 
Google Bug Hunters+1

5. 버그바운티 운영 방식에 따른 분류
기술 분야 외에도 연구 및 보상 방식에 따라 구분할 필요가 있다.
종류	설명
Public Bug Bounty	누구나 참여 가능한 공개 프로그램
Private Bug Bounty	초대받은 연구자만 참여 가능
Competitive Audit	정해진 기간에 여러 연구자가 코드 감사
Continuous Audit	지속적으로 특정 프로젝트의 보안 검토
Vulnerability Reward Program	기업이 직접 운영하는 취약점 보상 제도
Vulnerability Disclosure Program	취약점 신고 제도이며 보상이 보장되지 않음
Vulnerability Acquisition	취약점 구매 및 조정 공개 프로그램
Exploit Competition	지정된 대상에 대한 보안 연구 경연

주요 일반 버그바운티 플랫폼은 HackerOne, Bugcrowd, Intigriti, YesWeHack 등이 있다.
6. 프로젝트 지식베이스 분류 구조
앞서 설계한 GitHub 저장소의 knowledge/ 디렉터리를 다음과 같이 확장하는 것을 추천한다.
knowledge/
├── domains/
│   ├── web/
│   ├── web3/
│   │   ├── smart_contract/
│   │   ├── defi/
│   │   ├── blockchain_core/
│   │   ├── layer2/
│   │   ├── bridge/
│   │   └── wallet/
│   ├── windows/
│   │   ├── kernel/
│   │   ├── drivers/
│   │   ├── ipc/
│   │   ├── authentication/
│   │   ├── filesystem/
│   │   └── hypervisor/
│   ├── linux/
│   ├── browser/
│   ├── mobile/
│   ├── cloud/
│   ├── ai/
│   ├── binary/
│   ├── network/
│   ├── virtualization/
│   ├── hardware/
│   ├── supply_chain/
│   └── cryptography/
│
├── vulnerability_patterns/
│   ├── memory_safety/
│   ├── access_control/
│   ├── input_validation/
│   ├── concurrency/
│   ├── logic/
│   ├── state_management/
│   ├── cryptographic/
│   ├── economic/
│   └── isolation/
│
├── case_studies/
├── techniques/
├── references/
├── failure_patterns/
└── methodology/


취약점 패턴을 연구 분야와 별도로 분리한 이유는 서로 다른 분야에서 동일한 근본 원인이 등장하기 때문이다.
서로 다른 기술 분야에서도 공통적인 취약점 발생 원리를 재사용할 수 있는 구조
7. AI를 활용한 연구 관점에서의 분야 비교
분야	AI 활용 적합성	소스 확보 용이성	검증 환경 구축
Web3 Smart Contract	매우 높음	매우 높음	쉬움~보통
Open Source Web	매우 높음	매우 높음	쉬움~보통
AI Application	높음	높음	보통
Binary Open Source	높음	매우 높음	보통
Linux Kernel	높음	매우 높음	어려움
Windows Kernel	중간	낮음	어려움
Browser	높음	높음	어려움
Cloud	중간	낮음	어려움
Hardware	낮음~중간	낮음	매우 어려움

AI 활용 적합성은 코드 접근성, 컨텍스트 구성 비용, 검증 자동화 가능성을 기준으로 평가한 것이다.
8. 너에게 추천하는 연구 분야
기존 Pwnable 및 메모리 취약점 분석 경험과 현재 진행 중인 Solidity·EVM 공부를 고려하면, 다음 세 분야를 중심으로 프로젝트를 운영하는 것을 추천한다.
Web3 · DeFi

연구 비중 45%


소스코드 기반 분석, 경제적 로직, 스마트 컨트랙트 보안. AI와 협업하여 연구하기 좋은 분야.

Windows · System

연구 비중 35%


커널, 드라이버, 운영체제 내부 구조. 장기적인 전문 보안 연구 역량 확보.

Web · AI Application

연구 비중 20%


기존 웹 보안 경험 활용, 분석 자동화, 상대적으로 짧은 연구 피드백 주기.

Web3는 단기적인 실전 연구 분야로, Windows는 장기적인 전문 연구 분야로 설정하는 것을 추천한다. 특히 Web3는 공개 소스코드와 로컬 검증 환경이 풍부하기 때문에 지금 구축하려는 AI 기반 보안 연구 시스템의 성능을 평가하고 개선하기에도 적합하다.