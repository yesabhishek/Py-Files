Scores={
    "Dhoni":57,
    "rohit":107,
    "virat":97,
    "Sachin":99
    }
i=(input("Enter the key : \n"))
# for j in Scores:
#     if(i in Scores):
#         print("The key "+(i)+" exixts")
#         break
#     else:
#         print("No the key doesnt exixst")
#         break
        
    
s = {score for score in Scores if score == i}
print(s)
    