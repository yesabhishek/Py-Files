strr=input("Enter the String :")
strr=strr.lstrip()
strr=strr.rstrip()
j=0

# for cases like hello      abhishek

for i in strr:
    if (str(i)==' '):
        j=j+1
        if(j>1):
            continue
        print(i,end='')
    else:
        print(i,end='')
        

