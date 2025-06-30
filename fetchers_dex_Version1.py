from models.token import Token
from datetime import datetime, timedelta

async def fetch_new_tokens():
    # Dummy: Replace with real API call
    return [
        Token(
            id="0xdummy1",
            symbol="DOGEAI",
            chain="ETH",
            created_at=datetime.now() - timedelta(minutes=1),
            liquidity_usd=2500,
            liquidity_lock_until=datetime.now() + timedelta(days=90),
            fdv_usd=1000000,
            tx_10m=100,
            can_sell=True,
            dev_wallet_pct=3.0,
            hype_tweets_15m=30,
            hype_trend_delta=12.0,
            url="https://dexscreener.com/eth/0xdummy1"
        )
    ]