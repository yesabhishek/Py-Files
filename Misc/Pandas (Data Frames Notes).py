Python Codes for Data Frames


import pandas as pd

df=pd.read(..path)  --- data frame= pandas.read
df 
print(df)


df.shape 	--- shows the total no of rows and columns
df.info() 	--- shows the rrows and columns along with the data type


pd.set_option('display.max_columns',85)  --- display the amount of columns you give as an arguement 
pd.set_option('display.max_rows',85)  --- display the amount of rows you give as an arguement 

schema=pd.read(..path)
schema or print(schema)


df.head()  ---display top 5 or put in some values inside
df.tail()  ---display end 5 ...........................


