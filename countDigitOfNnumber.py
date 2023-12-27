n=int(input("Enter a number "))
i=0
p=1
while p!=0:
    p=n//10
    n=p
    i+=1
print("The total digit is ",i)






"""n=int(input("Enter a number "))
i=0
while n!=0:
    n//=10
    i+=1
print(i)
"""