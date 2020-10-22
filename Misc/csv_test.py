import csv
import pandas as pd

f=open("test.txt")
x=f.readlines()
s=[]
for i in x:
     i=i.replace(","," ")
     j=i.replace(" ",",")
     s.append(j)

#csvex=csv.writer(open("txt_csv","w"),delimiter=',',quoting=csv.QUOTE_ALL)
#csvex.writerow(s)
#
#
#read_file = pd.read_csv (r'C:\Users\achoud3\Py Files\txt_csv.csv')
#read_file.to_excel (r'C:\Users\achoud3\Py Files\new_xls.xlsx', index = None, header=True)

