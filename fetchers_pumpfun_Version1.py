from models.token import Token
from datetime import datetime, timedelta

async def fetch_new_pumpfun():
    # Dummy: Replace with real API call
    return [
        Token(
            id="pumpfun-dummy1",
            symbol="PEPEMOON",
            chain="SOL",
            created_at=datetime.now() - timedelta(minutes=2),
            liquidity_usd=4000,
            liquidity_lock_until=datetime.now() + timedelta(days=35),
            fdv_usd=2300000,
            tx_10m=85,
            can_sell=True,
            dev_wallet_pct=2.0,
            hype_tweets_15m=45,
            hype_trend_delta=19.0,
            url="https://pump.fun/PEPEMOON"
        )
    ]