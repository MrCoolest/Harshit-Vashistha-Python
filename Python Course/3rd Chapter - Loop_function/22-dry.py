a=int(input('Guess the number between 1 to 100:'))
import random
win=random.randint(1,100)
guess_times=1
while True: #2nd way to complete this code
    if a==win:
        print(f'CONGRATS YOU WIN!!!!!!! in {guess_times} times.')
        break
    else:
        if a>win:
            print('Its High')
        else:
            print('Its Low') 
    guess_times+=1 #this is called as dry code
    a=int(input('Guess again:'))           