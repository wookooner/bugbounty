import json
from datetime import datetime, timezone
import requests

GAMMA_API = "https://gamma-api.polymarket.com"
DATA_API = "https://data-api.polymarket.com"


def get_available_categories(limit: int = 30) -> list[dict]:
    """폴리마켓에서 사용 중인 영역(태그/카테고리) 목록을 조회합니다."""
    resp = requests.get(f"{GAMMA_API}/tags", params={"limit": limit}, timeout=10)
    resp.raise_for_status()
    return resp.json()


def fetch_markets_by_category(
    category_keyword: str,
    max_events: int = 100,
    min_volume_24h: float = 10000.0,
) -> list[dict]:
    """
    특정 영역(예: 'Politics', 'Crypto', 'Economy', 'Tech', 'AI')의
    활성 마켓 데이터를 거래량 순으로 추출합니다.
    """
    collected = []
    offset = 0
    page_size = 50
    keyword_lower = category_keyword.lower()

    while offset < max_events:
        resp = requests.get(
            f"{GAMMA_API}/events",
            params={
                "closed": "false",
                "limit": page_size,
                "offset": offset,
                "order": "volume24hr",
                "ascending": "false",
            },
            timeout=10,
        )
        resp.raise_for_status()
        events = resp.json()
        if not events:
            break

        for event in events:
            # 이벤트에 달린 태그 목록에서 원하는 영역 필터링
            tags = event.get("tags") or []
            tag_names = [
                f"{t.get('label', '')} {t.get('slug', '')}".lower() for t in tags
            ]
            title_lower = event.get("title", "").lower()

            is_match = any(keyword_lower in t for t in tag_names) or (
                keyword_lower in title_lower
            )
            if not is_match:
                continue

            for m in event.get("markets") or []:
                vol_24h = float(m.get("volume24hr") or 0)
                if vol_24h < min_volume_24h:
                    continue

                # outcomes와 outcomePrices는 JSON 문자열 형태로 반환됨
                outcomes = json.loads(m.get("outcomes") or "[]")
                prices = json.loads(m.get("outcomePrices") or "[]")
                if len(outcomes) < 2 or len(prices) < 2:
                    continue

                yes_prob = float(prices[0]) * 100  # Yes 가격 = 시장이 보는 확률(%)
                price_change_24h = float(m.get("oneDayPriceChange") or 0) * 100

                collected.append(
                    {
                        "category": category_keyword,
                        "event_title": event.get("title"),
                        "question": m.get("question"),
                        "condition_id": m.get("conditionId"),
                        "yes_prob_pct": round(yes_prob, 2),
                        "change_24h_pct": round(price_change_24h, 2),
                        "volume_24h_usd": round(vol_24h, 2),
                        "liquidity_usd": round(float(m.get("liquidity") or 0), 2),
                    }
                )

        offset += page_size

    # 24시간 거래량 내림차순 정렬
    collected.sort(key=lambda x: x["volume_24h_usd"], reverse=True)
    return collected


def detect_information_signals(
    markets: list[dict], min_abs_change_pct: float = 5.0
) -> list[dict]:
    """
    뉴스 보도 전 내부 정보/선반영 가능성이 높은 마켓 탐지:
    거래량이 받쳐주면서 24시간 내 확률이 급변한 마켓을 추출합니다.
    """
    signals = [
        m for m in markets if abs(m["change_24h_pct"]) >= min_abs_change_pct
    ]
    signals.sort(key=lambda x: abs(x["change_24h_pct"]), reverse=True)
    return signals


def fetch_whale_trades(
    condition_id: str, min_bet_usd: float = 1000.0, limit: int = 100
) -> list[dict]:
    """
    특정 마켓(condition_id)에 실제로 들어온 최근 대형 베팅(고래 체결 내역)을 조회합니다.
    누가 어떤 방향(Yes/No)에 얼마를 걸었는지 확인할 수 있습니다.
    """
    resp = requests.get(
        f"{DATA_API}/trades",
        params={"market": condition_id, "limit": limit},
        timeout=10,
    )
    resp.raise_for_status()
    trades = resp.json()

    whale_bets = []
    for t in trades:
        size = float(t.get("size") or 0)
        price = float(t.get("price") or 0)
        usd_value = size * price

        if usd_value < min_bet_usd:
            continue

        ts = t.get("timestamp")
        time_str = (
            datetime.fromtimestamp(int(ts), tz=timezone.utc).strftime(
                "%Y-%m-%d %H:%M:%S UTC"
            )
            if ts
            else "N/A"
        )

        whale_bets.append(
            {
                "time": time_str,
                "side": t.get("side"),  # BUY 또는 SELL
                "outcome": t.get("outcome"),  # Yes 또는 No
                "bet_usd": round(usd_value, 2),
                "implied_prob_pct": round(price * 100, 1),
                "wallet": t.get("proxyWallet") or t.get("user", "unknown"),
            }
        )

    return whale_bets


if __name__ == "__main__":
    # 1. 관심 영역 지정 (Politics, Crypto, Economy, Tech, Geopolitics 등)
    TARGET_DOMAINS = ["Politics", "Crypto", "Economy", "Tech"]

    for domain in TARGET_DOMAINS:
        print(f"\n==================== [{domain}] 영역 주요 마켓 ====================")
        markets = fetch_markets_by_category(
            category_keyword=domain, max_events=150, min_volume_24h=20000
        )

        for m in markets[:5]:
            print(
                f"- {m['question']}\n"
                f"  현재확률(Yes): {m['yes_prob_pct']}% | 24h변동: {m['change_24h_pct']:+.2f}% | "
                f"24h거래량: ${m['volume_24h_usd']:,.0f}"
            )

        # 2. 해당 영역에서 24시간 내 확률이 5%p 이상 급변한 마켓(정보 선반영 후보) 탐지
        signals = detect_information_signals(markets, min_abs_change_pct=5.0)
        if signals:
            top_signal = signals[0]
            print(f"\n  [!] 이상 신호 포착: '{top_signal['question']}' ({top_signal['change_24h_pct']:+.2f}%)")
            print("  --> 최근 $1,000 이상 대형 베팅 내역 추적:")

            # 3. 해당 마켓에 돈을 넣은 대형 베팅 내역 추출
            whales = fetch_whale_trades(
                condition_id=top_signal["condition_id"], min_bet_usd=1000.0
            )
            for w in whales[:5]:
                print(
                    f"      [{w['time']}] {w['side']} '{w['outcome']}' "
                    f"@ {w['implied_prob_pct']}% | 금액: ${w['bet_usd']:,.2f} | 지갑: {w['wallet'][:10]}..."
                )