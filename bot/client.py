import os
import time
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

client = Client(API_KEY, API_SECRET)

# Use Binance Futures Testnet
client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

# Synchronize time with Binance server
server_time = client.get_server_time()
system_time = int(time.time() * 1000)

client.timestamp_offset = server_time['serverTime'] - system_time