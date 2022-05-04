# AV key: GC6EUK3PIEELGNF4
import requests
import csv
#import pandas as pd
import io
from datetime import date

d1 = date.today().strftime("%d%m%Y")

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
_function = "FX_DAILY"
_from_symbol = "EUR"
_to_symbol = "USD"
_outputsize = "full" #optional
_datatype = "csv" #optional
_apikey = "GC6EUK3PIEELGNF4"
url = "https://www.alphavantage.co/query?function=" + _function \
  + "&from_symbol=" + _from_symbol \
  + "&to_symbol=" + _to_symbol \
  + "&outputsize=" +_outputsize \
  + "&datatype=" + _datatype \
  + "&apikey=" + _apikey

with requests.get(url, stream=True) as r:
    f = open('/Users/clayton/projects/Q/data/'+_from_symbol+_to_symbol+d1+'.csv', 'w')
    writer = csv.writer(f)
    lines = (line.decode('utf-8') for line in r.iter_lines())
    for row in csv.reader(lines):
        writer.writerow(row)
        #print(row)
    f.close()

