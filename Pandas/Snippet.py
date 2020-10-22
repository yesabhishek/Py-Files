import pandas as pd

df = pd.read_csv('..\Data\survey_results_public.csv')
#print(df.info())

print(df.head(10))

df.plot()
  