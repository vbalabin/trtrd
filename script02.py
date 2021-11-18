import json
import pprint
from credentials import config
import binance as bn
from jsondata import save_to_json
from binance.client import Client

SYM = "ETHUSDT"
PATH = "klines.json"
API_KEY = config.api_key
SECRET_KEY = config.secret_key
DEMA_SHORT = 20
DEMA_LONG = 50

client = bn.Client(API_KEY, SECRET_KEY)
klines = client.get_historical_klines(SYM, Client.KLINE_INTERVAL_1HOUR, "10 day ago UTC")
save_to_json(klines, PATH)
