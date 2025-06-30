import asyncio
import os
from config import settings
from fetchers.dex import fetch_new_tokens
from fetchers.pumpfun import fetch_new_pumpfun
from fetchers.twitter import fetch_tweet_hype
from fetchers.trends import fetch_trend
from models.token import Token
from scorer import score_token
from notifier import notify
from cache import SocialCache

FETCH_INTERVAL = settings.FETCH_INTERVAL
ALERT_SCORE = settings.ALERT_SCORE

cache = SocialCache()

async def main_loop():
    while True:
        tokens = []
        tokens.extend(await fetch_new_tokens())
        tokens.extend(await fetch_new_pumpfun())
        for token in tokens:
            if cache.is_alerted(token.id):
                continue
            token.hype_tweets_15m = await fetch_tweet_hype(token.symbol)
            token.hype_trend_delta = await fetch_trend(token.symbol)
            score = score_token(token)
            if score >= ALERT_SCORE:
                await notify(token, score)
                cache.mark_alerted(token.id)
        await asyncio.sleep(FETCH_INTERVAL)

if __name__ == "__main__":
    asyncio.run(main_loop())