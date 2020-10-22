string=input("Enter a string : \n")
string1 = ''
string2=string.swapcase()

'''for i in range(len(string)):
    
    if(string[i] >= 'a' and string[i] <= 'z'): 
        string1 = string1 + chr((ord(string[i]) - 32))
        
    elif(string[i] >= 'A' and string[i] <= 'Z'):
        string1 = string1 + chr((ord(string[i]) + 32))
        
    else:
        string1 = string1 + string[i]
'''
print(" The orginal string is : "+ string)
print(" The orginal string is : "+ string2)
