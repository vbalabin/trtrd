import pandas as pd
import binance as bn
from datetime import datetime
import matplotlib.pyplot as plt
from jsondata import save_to_json
from jsondata import load_json_to_dict
from binance.client import Client
from credentials import config
# plt.style.use("fivethirtyeight")

SYM = "ETHUSDT"
PATH = "klines.json"
API_KEY = config.api_key
SECRET_KEY = config.secret_key
DEMA_SHORT = 20
DEMA_LONG = 50

def download():
    client = bn.Client(API_KEY, SECRET_KEY)
    klines = client.get_historical_klines(SYM, Client.KLINE_INTERVAL_1HOUR, "10 day ago UTC")
    save_to_json(klines, PATH)


def convert_json_to_dicts(path):
    klines = list()
    for kl in load_json_to_dict(path):
        kd = {
            "DateTime": datetime.fromtimestamp(kl[0] // 1000),
            "Open": float(kl[1]),
            "High": float(kl[2]),
            "Low": float(kl[3]),
            "Close": float(kl[4]),
            "Volume": float(kl[5]),
        }
        klines.append(kd)
    return klines

def calculate_n_show():
    df = pd.DataFrame(convert_json_to_dicts("klines.json"))
    format = '%Y-%m-%d %H:%M:%S'
    df = df.set_index(pd.DatetimeIndex(df['DateTime']))

    print(df)

    def create_DEMA(df, time_period, column):
        EMA = df[column].ewm(span=time_period, adjust=False).mean()
        DEMA = 2 * EMA - EMA.ewm(span=time_period, adjust=False).mean()
        return DEMA

    df["DEMA_short"] = create_DEMA(df, DEMA_SHORT, "Close")
    df["DEMA_long"] = create_DEMA(df, DEMA_LONG, "Close")

    col_list = ["DEMA_long", "DEMA_short", "Close"]
    df[col_list].plot(figsize=(12.2, 6.4))
    plt.title("Close price")
    plt.ylabel("y label")
    plt.xlabel("x label")
    plt.show()

if __name__ == '__main__':
    #download()
    calculate_n_show()
