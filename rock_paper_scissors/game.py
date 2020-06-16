import random

pscore = 0
cscore = 0

def rock_paper_scissors(player_name, player, computer):
    global cscore
    global pscore
    if player == computer:
        print(f"TIE!!! Because computer selected {computer}")

    elif player == "Rock":
        if computer == "Paper":
            print(f"You Lose!!! Because computer selected {computer}")
            cscore += 1

        else:
            print(f"You Won!!! Because computer selected {computer}")
            pscore += 1

    elif player == "Paper":
        if computer == "Scissors":
            print(f"You Lose!!! Because computer selected {computer}")
            cscore += 1

        else:
            print(f"You Won!!! Because computer selected {computer}")
            pscore += 1

    elif player == "Scissors":
        if computer == "Rock":
            print(f"You Lose!!! Because computer selected {computer}")
            cscore += 1

        else:
            print(f"You Won!!! Because computer selected {computer}")
            pscore += 1
    
    else:
        print("Please select appropriate Input!!")


n = int(input("how manny rounds you want to play: "))
player_name = str(input("Enter name of player: ")).capitalize()

for _ in range(n):
    player = str(input("enter your choice(Rock, paper or scissors): ")).capitalize()
    temp = ['Rock', 'Paper', 'Scissors']
    computer = temp[random.randint(0,2)]
    rock_paper_scissors(player_name, player, computer)

print("\n")
print("  Score")
print(f"{player_name} : {pscore}  ")
print(f"Computer : {cscore}  ")
print("\n")

if pscore == cscore:
    print("TIE!!")

elif pscore > cscore:
    print(f"{player_name} Won! With Score of {pscore}")

else:
    print(f"Computer Won! With Score of {cscore}")