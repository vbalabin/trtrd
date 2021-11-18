import json
import binance as bn
import pprint
pp = pprint.PrettyPrinter(indent=4)
from credentials import config

client = bn.Client(config.api_key, config.secret_key)
status = client.get_system_status()

pp.pprint(status)
