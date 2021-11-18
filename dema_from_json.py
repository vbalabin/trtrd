from jsondata import load_json_to_dict
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
plt.style.use("fivethirtyeight")

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

df = pd.DataFrame(convert_json_to_dicts("klines.json"))
format = '%Y-%m-%d %H:%M:%S'
df = df.set_index(pd.DatetimeIndex(df['DateTime']))

print(df)

def create_DEMA(df, time_period, column):
    EMA = df[column].ewm(span=time_period, adjust=False).mean()
    DEMA = 2 * EMA - EMA.ewm(span=time_period, adjust=False).mean()
    return DEMA




df["DEMA_20"] = create_DEMA(df, 20, "Close")
df["DEMA_50"] = create_DEMA(df, 50, "Close")

col_list = ["DEMA_20", "DEMA_50", "Close"]
df[col_list].plot(figsize=(12.2, 6.4))
plt.title("Close price")
plt.ylabel("y label")
plt.xlabel("x label")
plt.show()