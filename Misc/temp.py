import csv

f=open("test.txt")
x=f.readlines()
s=[]
for i in x:
     i=i.replace(","," ")
     j=i.replace(" ",",")
     s.append(j)

csvex=csv.writer(open("txt_csv","w"),delimiter=',',quoting=csv.QUOTE_ALL)
csvex.writerow(s)

