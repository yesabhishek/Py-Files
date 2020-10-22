from collections import OrderedDict 


def remove(str): 
	return "".join(OrderedDict.fromkeys(str)) 


if __name__ == "__main__": 
	str =input()
	 
	print (remove(str)) 
