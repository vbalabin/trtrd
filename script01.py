from jsondata import load_json_to_dict
from datetime import datetime

klines = load_json_to_dict("klines.json")

kl = klines[0]

_dt = datetime.fromtimestamp(kl[0] // 1000)
print(_dt)
