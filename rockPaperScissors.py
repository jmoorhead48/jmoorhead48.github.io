#Python 3
#Rock, Paper, Scissors
#James Moorhead
#CS160
play = input("Would you like to Play 'Rock, Paper, Scissors'?\n Yes(y) or No (n)\n")
if play.lower() == ('y'):
    while play.lower() == ('y'):
        import random
        initial = input("Please pick one: Rock, Paper, Scissors.\n")
        user = initial.strip()
        computer = random.choice(['rock','paper','scissors'])
        if user.lower() == computer:
            print("DRAW!")
        elif user.lower() == ('rock'):
            if computer == ('paper'):
                print("You LOSE! :(")
            else:
                print("You WIN!!!! :D")
        elif user.lower() == ('paper'):
            if computer == ('scissors'):
                print("You LOSE! :(")
            else:
                print("You WIN!!!! :D")
        elif user.lower() == ('scissors'):
            if computer == ('rock'):
                print("you LOSE! :(")
            else:
                print("You WIN!!!! :D")
        play = input("Would you like to Play 'Rock, Paper, Scissors' again?\n Yes(y) or No (n)\n")
    print('Hope you enjoyed! :D')
else:
    print("What a wuss")

