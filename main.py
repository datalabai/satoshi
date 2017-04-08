import json
import pandas as pd


pd.set_option('display.expand_frame_repr', False)

url = 'https://api.coinmarketcap.com/v1/ticker/'
df = pd.read_json(url)
df.describe()
