print("Enter the marks  of three subjects")
a=int(input())
b=int(input())
c=int(input())
sum=a+b+c
s=sum/3
if s>=80 and s<=100:
    print("Grade A")
elif s>=70 and s<80:
    print("Grade B")
elif s>=60 and s<70:
    print("Grade C")
elif s>=40 and s<60:
    print("Grade D")
elif s<40:
    print("Grade E")




    