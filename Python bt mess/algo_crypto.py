# AV key: GC6EUK3PIEELGNF4
import requests
import csv
#import pandas as pd
import io
from datetime import date

d1 = date.today().strftime("%d%m%Y")

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
_function = "DIGITAL_CURRENCY_DAILY"
_symbol = "AVAX"
_market = "USD"
_datatype = "csv" #optional
_apikey = "GC6EUK3PIEELGNF4"
url = "https://www.alphavantage.co/query?function=" + _function \
  + "&symbol=" + _symbol \
  + "&market=" + _market \
  + "&datatype=" + _datatype \
  + "&apikey=" + _apikey

with requests.get(url, stream=True) as r:
    f = open('/Users/clayton/projects/Q/data/'+_symbol+d1+'.csv', 'w')
    writer = csv.writer(f)
    lines = (line.decode('utf-8') for line in r.iter_lines())
    for row in csv.reader(lines):
        writer.writerow(row)
        #print(row)
    f.close()

