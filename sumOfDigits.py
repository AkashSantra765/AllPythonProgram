n=int(input("Enter a number "))
a=0
while n!=0:
    p=n%10
    a+=p
    n//=10
print("The sum of digits is ",a)