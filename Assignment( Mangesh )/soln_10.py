#There cant be any duplicate keys in dictionary as new entries overwrites old entries

sample={1: 44, 2: 44, 2: 9, 4: 16, 5: 25, 6: 36}

for i in sample: 
    if(i ==sample.get(i)):
        
