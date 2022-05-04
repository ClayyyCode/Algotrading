# AV key: GC6EUK3PIEELGNF4
import requests
import csv
#import pandas as pd
import io
from datetime import date

d1 = date.today().strftime("%d%m%Y")

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
_function = "TREASURY_YIELD"
_interval = "daily"
_maturity = ["1month","3month","1year","2year","5year","10year","30year"]
_datatype = "csv" #optional
_apikey = "GC6EUK3PIEELGNF4"
for m in _maturity:
  url = "https://www.alphavantage.co/query?function=" + _function \
    + "&interval=" + _interval \
    + "&maturity=" + m \
    + "&datatype=" + _datatype \
    + "&apikey=" + _apikey

  with requests.get(url, stream=True) as r:
      f = open('/Users/clayton/projects/Q/data/UST'+m+d1+'.csv', 'w')
      writer = csv.writer(f)
      lines = (line.decode('utf-8') for line in r.iter_lines())
      for row in csv.reader(lines):
          writer.writerow(row)
          #print(row)
      f.close()

