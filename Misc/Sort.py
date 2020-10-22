input_string = input("Enter a list element separated by space ")
list  = input_string.split()
list.sort()
for i in list:
    print(i)
