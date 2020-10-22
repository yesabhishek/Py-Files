Number=int(input())
dup=Number
rev=0
while(dup!=0):
    div=dup%10;
    rev=rev*10+div
    dup=dup//10;
 
if(rev==Number):
    print('palindrome')
else:
    print(' Not a palindrome')


