user=int(input('Guess the correct number between 100:'))
won=19
over=False
i=1
while not over:
    if won==user:
        print(f'Congratulation You won !!!!!, This is you\'r {i} times.')
        over=True
    else:
        if user>won:
            print('Its high')
            user=int(input('guess again:'))
            i+=1
        else:
            print('Its low') 
            user=int(input('guess again:')) 
            i+=1      
        #this games have many types coding