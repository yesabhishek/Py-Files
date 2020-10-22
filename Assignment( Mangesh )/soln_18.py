f=open("first.py")
lines=0
words=0
for i in f:
    lines=lines+1
    words=words+len(i)
for j in f:
     print(j +":"+str(f.count(j)))
print(str(lines)+" lines present in the file ")
print(str(words)+" words present in the file ")
f.close()
