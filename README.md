# Telegram Memecoin Alert Bot

## Overview

A modular async Python bot that detects trending memecoins/tokens (DEX, Pump.fun, Twitter, Google Trends) and notifies on Telegram when safe/hyped coins appear.

## Features

- Modular fetchers (DEX, Pump.fun, Twitter, Google Trends)
- Unified Token model (Pydantic)
- Heuristic scoring (liquidity, hype, safety)
- Telegram notification (aiogram3)
- Extensible, production-ready structure

## Quick Start

1. **Clone this repository**
2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```
3. **Copy and edit .env**
   ```bash
   cp .env.example .env
   ```
   Fill in your Telegram bot token, chat id, etc.

4. **Run the bot**
   ```bash
   python bot.py
   ```

## Project Structure

```
.
├── bot.py            # Main async loop
├── config.py         # Loads env vars
├── .env.example      # Copy to .env and fill
├── fetchers/
│   ├── __init__.py
│   ├── dex.py
│   ├── pumpfun.py
│   ├── twitter.py
│   └── trends.py
├── models/
│   ├── __init__.py
│   └── token.py
├── scorer.py
├── cache.py
├── notifier.py
├── requirements.txt
└── README.md
```

## .env Example

```
TG_TOKEN=your-telegram-bot-token
TG_CHAT=your-chat-id
TW_BEARER=your-twitter-token
FETCH_INTERVAL=60
ALERT_SCORE=0.8
LIQ_MIN_USD=2000
LOCK_DAYS_MIN=30
```

## LICENSE

MIT
