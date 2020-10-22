string=input("Enter the string")
find=input("Enter the stirng to find : ")
c=string.count(find)
if(c==0):
    print("The string is not found in the original string ")
else:
    print("The string is found "+str(c)+" many times in a string") 
    
