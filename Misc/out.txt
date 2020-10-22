arrangement={
    "1":1,
    "2":2,
    "3":5,
    "7":4,
    "9":0
    }
print(" The dictionary is : \n")
print(arrangement)
l=[]

# converting the dictionary to list
for i in arrangement:
    l.append(arrangement.get(i))
   
    

print("Sorting in Ascending order: \n")
l.sort()
print(l)
print("Sorting in Descending order: \n")
l.sort(reverse=True)
print(l)


