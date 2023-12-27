n=int(input("Enter the year"))
if(n%400==0)and(n%100==0):
    print("This year is leap year")
elif(n%4==0)and(n%100!=0):
    print("This year is leap year")
else:
    print("This year is not leap year")