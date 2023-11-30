import random
ComputerScore=0
PlayerScore=0
round=0
while True:
    if ComputerScore==3:
        print("Computer Win")
        break
    elif PlayerScore==3:
        print("!!!YOU WIN THE GAME!!!")
        break
    CC = random.choice(["R", "S", "P"])
    round+=1
    print(f"Round:{round}")
    while True:
        PC = (input("Please choice Rock:R, Scissor:S, Papper:P")).upper()
        if PC in ["P","R","S"]:
           break
        else:
            print("Invalid input please input R , S , P")
    if CC==PC:
        print(f"Computer Choice{CC}")
        print("You are same try again")
    elif (PC=="R" and CC=="S") or (PC=="S" and CC=="P") or (PC=="P" and CC=="R"):
        print(f"Computer Choice{CC}")
        PlayerScore += 1
        print(f"You win your score: {PlayerScore}")
    else:
        ComputerScore += 1
        print(f"Computer choice {CC}")
        print(f"Computer win Computer score: {ComputerScore}")




