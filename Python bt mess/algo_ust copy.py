# AV key: GC6EUK3PIEELGNF4
import requests
import csv
import pandas as pd
import io
from datetime import date
from io import StringIO
import matplotlib as plt

d1 = date.today().strftime("%d%m%Y")


url = "http://localhost:3001/?QQQ"

with requests.get(url, stream=True) as r:
        QQQ = (pd.read_csv(StringIO(r.text)))

#plt.plot(QQQ.loc["close"])
plt.plot([1,2,3,4])
plt.ylabel("date")
plt.show()
