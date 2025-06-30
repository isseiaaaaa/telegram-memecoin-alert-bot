import asyncio
from aiogram import Bot
from config import settings

bot = Bot(token=settings.TG_TOKEN, parse_mode="HTML")

async def notify(token, score):
    msg = (
        f"🚀 <b>{token.symbol}</b> is exploding!\n"
        f"Score: {score:.2f}  |  Tweets(15m): {token.hype_tweets_15m}\n"
        f"Liq: ${token.liquidity_usd:,.0f}  |  FDV: ${token.fdv_usd or 0:,.0f}\n"
        f"Google Trend Δ: {token.hype_trend_delta:+.2f}\n"
        f"<a href='{token.url}'>Live chart</a>"
    )
    await bot.send_message(settings.TG_CHAT, msg)