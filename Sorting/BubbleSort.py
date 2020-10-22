if __name__ == "__main__":
    
    unsorted  = [64, 34, 25, 12, 22, 11, 90]
    unsorted1 = [-1, -5, 0, 7, 4, 1, 11]
    print(unsorted)


    size = len(unsorted)
    for i in range(0,size):
        for j in range(0,size-1):
            if unsorted[j+1] < unsorted[j]: unsorted[j+1], unsorted[j]  = unsorted[j], unsorted[j+1]
 
    print(unsorted)    
