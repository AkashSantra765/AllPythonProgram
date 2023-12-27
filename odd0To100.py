start=int(input("Enter the first number"))
end=int(input("Enter the last number"))
print("The odd number is ")
for i in range(start,end+1):
    if i%2!=0:
        print(i)
