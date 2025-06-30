from config import settings

def score_token(token, prob_rug=None):
    from datetime import datetime, timedelta
    if (
        token.liquidity_usd < settings.LIQ_MIN_USD
        or (token.liquidity_lock_until and (token.liquidity_lock_until-token.created_at).days < settings.LOCK_DAYS_MIN)
        or not token.can_sell
        or (token.dev_wallet_pct is not None and token.dev_wallet_pct > 5)
    ):
        return 0
    base = min(token.tx_10m / 50, 1)
    social = min(token.hype_tweets_15m / 100, 1) * 0.6 + min(token.hype_trend_delta / 30, 1) * 0.4
    final = base * (1 + social)
    if prob_rug is not None and prob_rug > 0.5:
        final = 0
    return final