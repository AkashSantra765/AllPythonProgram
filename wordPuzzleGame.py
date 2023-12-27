l1=["FATHER","BREAK","GREEN","AEROPLANE","AKASH"]
l2=["RAEHTF","KABRE","RENEG","OAERELANP","HKASA"]
s=0
for i in range(5):
    print("Arrange the letters to from a valid word:")
    print(l2[i])
    n=input()
    print()
    if l1[i]==n.upper():
        s+=1
        print("Correct")
    else:
        s-=1
        print("Wrong")
    print()
print("Net score is ",s)