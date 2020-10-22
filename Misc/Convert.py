tmp = str(2007365)
dFormat='9999-12-31'
if tmp =='' or tmp ==' ':
     print(dFormat)
else:
     try:
          tmp=tmp.zfill(7)
          d1=int(tmp[-3:])
          y1=int(tmp[:4])
     except ValueError:
          print(dFormat)
if tmp =='0000000':
     print(dFormat)
elif d1 > 366:
     print(dFormat)
else:
     month = 1
     try:
          while d1 - calendar.monthrange(y1,month)[1] > 0 and month <= 12:
               d1 = d1 - calendar.monthrange(y1,month)[1]
               month = month + 1
     except:
          print(dFormat)
     month=str(month).zfill(2)
     d1=str(d1).zfill(2)
     sFormat="'"+str(str(y1)+'-'+month+'-'+d1)+"'"
print(sFormat)
