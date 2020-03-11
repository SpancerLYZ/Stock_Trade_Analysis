import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
style.use('ggplot')
start = dt.datetime(2015, 1, 1)
end = dt.datetime.now()
df = web.DataReader("002901.SZ", 'yahoo', start, end)
df.reset_index(inplace=True)
# df.set_index("Date", inplace=True)
# df = df.drop("Symbol", axis=1)
print(df.tail(6))
# Above is the first class, to get those data
