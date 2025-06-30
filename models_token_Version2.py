from pydantic import BaseModel, AnyHttpUrl
from typing import Literal, Optional
from datetime import datetime

class Token(BaseModel):
    id: str
    symbol: str
    chain: Literal["ETH","SOL","BSC"]
    created_at: datetime
    liquidity_usd: float
    liquidity_lock_until: Optional[datetime]
    fdv_usd: Optional[float]
    tx_10m: int
    can_sell: bool
    dev_wallet_pct: Optional[float]
    hype_tweets_15m: int
    hype_trend_delta: float
    url: AnyHttpUrl