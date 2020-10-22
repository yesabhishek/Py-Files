import random

file = open('grades.txt', 'w')
#filename = "grades.csv"
randomlist = []

for i in range(1,200):
    n = random.randint(5,10)
    randomlist.append(n)
print(randomlist)




