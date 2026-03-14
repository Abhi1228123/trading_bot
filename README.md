# trading_bot

# Binance Futures Testnet Trading Bot

A Python CLI application that places Market and Limit orders on Binance Futures Testnet (USDT-M). The bot supports BUY/SELL orders, input validation, logging, and error handling.

## Project Structure

trading_bot
│
├── bot
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs
│   └── trading.log
│
├── cli.py
├── requirements.txt
└── README.md

## Setup Instructions

1. Clone the repository

git clone https://github.com/yourusername/trading_bot.git
cd trading_bot

2. Create a virtual environment

python -m venv venv

3. Activate the environment

Windows:
venv\Scripts\activate

4. Install dependencies

pip install -r requirements.txt

## Environment Variables

Create a .env file and add:

API_KEY=your_api_key

API_SECRET=your_api_secret

## How to Run the Program

Market Order

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002

Limit Order

python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.002 --price 67500

## Logging

Logs are stored in:

logs/trading.log

The log file records:

- API requests
- API responses
- errors

  ## Assumptions

- Binance Futures Testnet account is active
- API key has Futures permission enabled
- Minimum order size must be >= 100 USDT

  ## Technologies Used

  Python 3
python-binance
argparse
logging
python-dotenv
  

