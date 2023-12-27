print("1.Addition\n","2.Subtraction\n","3.Multiplication\n","4.Division")
n=int(input("Enter the value what you want "))
a=int(input("Enter first number "))
b=int(input("Enter second number "))
match n:
    case 1:
        print("After addition the results is ",a+b)
    case 2:
        print("After subtraction the results is ",a-b)
    case 3:
        print("After multiplecation the results is ",a*b)
    case 4:
        print("After division the results is ",a/b)