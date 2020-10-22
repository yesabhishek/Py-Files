import random
#import pdb

number=int(input("Enter a number between 1 and 100 \n"))

if(number >100):
    print("Invalid Number Pressed -_- ")
    exit()
alpha=int(number)
number=random.randint(1,100)
i=0

#pdb.set_trace()
while(alpha!=number):
    i+=1
    if(alpha>number):
        print("Too high \n")
        alpha=int(input("Enter again \n"))
    if(alpha<number):
        print("Too Low")
        alpha=int(input("Enter again \n"))
    if(alpha==number):
        print(" You won in "+str(i)+" attempts *_* ")
        break
        
    
