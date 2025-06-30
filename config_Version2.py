import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    TG_TOKEN: str = os.getenv("TG_TOKEN", "")
    TG_CHAT: str = os.getenv("TG_CHAT", "")
    TW_BEARER: str = os.getenv("TW_BEARER", "")
    FETCH_INTERVAL: int = int(os.getenv("FETCH_INTERVAL", "60"))
    ALERT_SCORE: float = float(os.getenv("ALERT_SCORE", "0.8"))
    LIQ_MIN_USD: int = int(os.getenv("LIQ_MIN_USD", "2000"))
    LOCK_DAYS_MIN: int = int(os.getenv("LOCK_DAYS_MIN", "30"))

settings = Settings()