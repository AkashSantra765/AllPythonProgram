n=input("Enter a number")
s=n[::-1]
s=int(s)
n=int(n)
if n==s:
    print("It is palindrome ")
else:
    print("It is not palindrome")