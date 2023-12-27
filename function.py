#simple function print
def printN():
    print("MySirG")
printN()


#A function which excepts two arguments and print them in function body
def args(a,b):
    print("A is ",a," and B is ",b)
args(3,5)


#A function which excepts an unknown number of arguments
def Args(*args):
    for i in args:
        print(i)
    #print(type(args)) 
Args(2,3,5,6,7,8,9)


