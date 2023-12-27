n=int(input("Enter a number"))
tem=n
rev=0
while(n>0):
    m=n%10
    rev=rev*10+m
    n=n//10
if(tem==rev):
    print("The number is palindrome!")
else:
     print("Not a palindrome!")


    
    