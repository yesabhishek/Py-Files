from itertools import permutations 

	
string = 'ABC'
permu = permutations(string)

for i in list(permu): 
    print (''.join(i)) 
		

