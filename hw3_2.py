'''
Yili Lin
2/19/2019
I have not given or received any unauthorized assistance on this assignment.
'''

from hw3_1 import *

def getinputbetnum(balance):
    'input the bet number limit the input to positive number'
    while True:
        try:
            global betnum
            betnum= eval(input('How much would you like to bet?'))
            if betnum > balance:
                raise ValueError('You cannot bet more than your balance.')
            elif betnum < 0:
                raise ValueError('You cannot bet less than 0.')
        except ValueError as error:
            print(error)
        except NameError:
            print('You can only enter a number.')
        else:
            break

def getinputdice():
    'input the number of dice and limit the input to integer'
    while True:
        try:
            global sixdice
            sixdice= int(input('How many six sides dices would you like to play?'))
            if sixdice < 0:
                raise NameError('You cannot enter than 0.')
        except NameError as error:
            print(error)
        except ValueError:
            print('You can only enter a integer.')
        else:
            break

    while True:
        try:
            global tendice
            tendice= int(input('How many ten sides dices would you like to play?'))
            if tendice < 0:
                raise NameError('You cannot enter than 0.')
        except NameError as error:
            print(error)
        except ValueError:
            print('You can only enter a integer.')
        else:
            break

    while True:
        try:
            global twentydice
            twentydice= int(input('How many twenty sides dices would you like to play?'))
            if twentydice < 0:
                raise NameError('You cannot enter than 0.')
        except NameError as error:
            print(error)
        except ValueError:
            print('You can only enter a integer.')
        else:
            break





def game():
    'a dice game'
    name=input('what is you name?')
    balance=100
    while balance >0:
        print(f'{name} you have ${balance} balance.')
        while True:#limit the input of Y/N
            answer=input('Would you like to play a game? Answer Y/N')
            if answer.lower() not in ('y','n'):
                print ('You can only enter Y/N')
            else:
                break
        if answer.lower()=='y':
            goal=random.randrange(1,101)
            print(f'Your goal is {goal}')
            # input how much to bet
            getinputbetnum(balance)
            # input the number of dice to bet
            getinputdice()
            #get the new balance
            balance-=betnum
            cup=Cup(sixdice,tendice,twentydice)
            # roll the dice
            cup.roll()
            # get the sum of dice
            facevalue=cup.getSum()
            print(f'You roll {facevalue}.')
            if facevalue == goal:  # win 10 times
                balance += 10 * betnum
                print(f'You win 10 times of you bet. You win ${10 * betnum}.')
            elif facevalue in range(goal - 5, goal):  # win 5 times
                balance += 5 * betnum
                print(f'You win 5 times of you bet. You win ${5 * betnum}.')
            elif facevalue in range(goal - 10, goal):  # win 2 times
                balance += 2 * betnum
                print(f'You win 2 times of you bet. You win ${2 * betnum}.')
            else:
                print(f'You lose ${betnum}.')
        else:
            print('Have a good day. Bye.')
            break
    else:
        print("You don't have any balance. Bye.")











