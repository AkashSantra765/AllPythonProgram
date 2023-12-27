def isPalindrome(s):
    return s == s[::-1]
 
s=input("Enter a string")
ans = isPalindrome(s)
 
if ans:
    print("String is palindrome")
else:
    print("String is not palindrome")

'''Another method of string palindrome or not '''

n=input("Ener the String")
s=n[::-1]
if n==s:
    print("String is palindrome")
else:
    print("String is not palindrome")