#Python 3
#Mastermind
#James Moorhead
#CS160
import random
##initiating empty master compare list##
master = []
##initiating empty guess list##
guess = []
##this is computers random start code##
while len(master) <4:
    master.append(random.choice(['r','g','b','y']))
##get user input
first =(input('Please guess the 4 secret colors! (Valid Guesses Include: R, G, B, Y) '))
for i in (first):
    guess.append(i)
for i , j in enumerate(master):
    print(i,j)
print(guess)
print(master)
