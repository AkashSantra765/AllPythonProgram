lower=int(input("Enter the lower value"))
upper=int(input("Enter the upper value"))
for i in range(lower, upper + 1):
    order = len(str(i))
    sum = 0
    temp = i
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10 
        if i == sum: 
          print(i)