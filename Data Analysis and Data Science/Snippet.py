import pandas as pd
from matplotlib import pyplot as plt

plt.close('all')

df = pd.read_csv('DataSets\\avocado.csv')
df['Date'] = pd.to_datetime(df["Date"])
albany_df = df[df["region"] == "Albany" ]
albany_df.set_index("Date", inplace=True)

print(albany_df.plot())




