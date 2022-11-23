import random

def get_computer_choice():
    global Computer
    list = ['rock','paper','scissors',]
    Computer = random.choices(list)
    Computer = Computer[0]
    return(Computer)

def get_user_choice():
    global User
    User = input('Enter a result:(rock,paper,scissors): ')
    print(f'{User}')
    return(User)

def get_winner(User,Computer):
    if User == Computer:
        print("Tie")
    elif User == "rock" :
        if Computer == "scissors":
            print('You wins')
        elif Computer == "paper":
            print('You lost')
        else:
            print("Invalid input")
    elif User == "paper" :
        if Computer == "scissors":
            print('You lost')
        elif Computer == "rock":
            print('You wins')
        else:
            print("Invalid input")
    elif User == "scissors" :
        if Computer == "rock":
            print('You lost')
        elif Computer == "paper":
            print('You wins')
        
        else:
            print("Invalid input")
    elif User ==  Computer:
        print("It is a tie")
    else:
        print("Invalid input")

def let_play():

    get_computer_choice()
    get_user_choice()
    get_winner(User,Computer)
    pass

let_play()