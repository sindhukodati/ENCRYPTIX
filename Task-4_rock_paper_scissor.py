import random
choices= ['rock', 'paper', 'scissors']
while True:
    u_choice = input('Enter your choice from list (rock, paper or scissors): ')
    p_choice = random.choice(choices)
    print(f"Your choice is {u_choice}, computer choice is y {p_choice}\n")
    if u_choice == p_choice:
        print(f"Both players selected {u_choice}.So It's a tie!")
    elif u_choice == "rock":
        if p_choice == "scissors":
            print("You won! because Rock smashes scissors.")
        else:
            print("You lost :( Paper covers rock!")
    elif u_choice == "paper":
        if p_choice == "rock":
            print("You won! because Paper covers rock.")
        else:
            print("You lost :( Scissors cuts paper!")
    elif u_choice == "scissors":
        if p_choice == "paper":
            print("You won! because Scissors cuts paper.")
        else:
            print("You lost :( Rock smashes scissors!")
            
    p_again = input('Play again?(y/n)')
    if (p_again.lower() == 'n'):
        break
