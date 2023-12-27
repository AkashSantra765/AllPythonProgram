print("You have three chance")
for i in range(3):
    n=int(input(("Enter an even number ")))
    if n%2!=0:
        print("WRONG !")
    else:
        print("WINNER")
        break
else:
    print("You lost the game")