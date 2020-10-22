""" The purpose of zip() is to map the 
similar index of multiple containers so that they can be used just using as single entity. """

A = ["Alpha", "Beta", "Gamma"]
B = [1000, 2000, 3000]

Result = zip(A,B)

print(dict(Result))
#print(list(Result))