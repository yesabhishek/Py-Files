sample={1: 44, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
max=0
min=sample.get(1)

#finding the max VALUE
for i in sample:
    if(max<sample.get(i)):
        max=sample.get(i)

#finding the min VALUE
for i in sample:
    if(min>sample.get(i)):
        min=sample.get(i)

print(" The max value is "+ str(max)+" and the min value is "+str(min)) 
