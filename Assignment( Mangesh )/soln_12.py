sample= {1:2,3:9}
sample2= {2:2,2:18}

for i in sample:
    for j in sample2:
        if(i==j):
            i=(sample.get(i)+sample2.get(i))
sample.update(sample2)
print(sample)






'''if(sample.get(i)==sample2.get(i)):
        i=(sample.get(i)+sample2.get(i))
sample.update(sample2)
print(sample)'''
