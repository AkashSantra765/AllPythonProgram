n=input("Enter a string ")
for x in n:
    if x=='r':
        break
    print(x,end='')
else:
    print("all the character are processed ")