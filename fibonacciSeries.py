n=int(input("Enter a number "))
a=0
b=1
for i in range(n):
    c=a+b
    print(a)
    a=b
    b=c
   