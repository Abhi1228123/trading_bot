# trading_bot
1️⃣ Setup Steps

Example:

python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
2️⃣ How to Run

Market order example:

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002

Limit order example:

python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.002 --price 67500
3️⃣ Assumptions

Example:

Binance Futures Testnet account is active

API key has Futures permission enabled

Minimum order value must be ≥ 100 USDT
