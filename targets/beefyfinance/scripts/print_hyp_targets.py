with open(r"targets/beefyfinance/research_logs/2026-11-24-full-fn-bodies.md", encoding="utf-8") as f:
    text = f.read()

sections = text.split("\n### ")
wanted = ("beefInETH", "beefIn", "_swapAndStake", "_returnAssets", "harvest", "chargeFees", "addLiquidity")
for sec in sections[1:]:
    header = sec.splitlines()[0]
    if any(header.startswith(f"`{w}`") for w in wanted):
        print("\n### " + sec)
