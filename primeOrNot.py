n=int(input("Enter a number "))
if n > 1:
    for i in range(2, int(n/2)+1):
        if (n % i) == 0:
            print("Not prime number")
            break
    else:
        print("Prime number")
else:
    print("Not a prime number")