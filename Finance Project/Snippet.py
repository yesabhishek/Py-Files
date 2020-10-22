import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader.data as web


plt.style.use('ggplot')

start = dt.datetime(2000,1,1)
end = dt.datetime(2019,12,25)

df = web.DataReader('TSLA', 'yahoo', start, end)
#print(df.head(20))

#df.to_csv('tsla.csv')
 
df[['High','Low','Adj Close']].plot()
plt.show()