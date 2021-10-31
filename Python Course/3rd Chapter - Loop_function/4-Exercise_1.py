#a=int(input('Enter first number:'))
#b=int(input('Enter Second number:'))
#c=int(input('Enter third number:'))
#if a>b:
 #   if a>c:
  #      print(f'{a} is greater')
   # else:
    #    print(f'{c} is greater')
#else:
 #   if b>c:
  #      print(f'{b} is greater')
   # else:
    #    print(f'{c} is greater')       

win = 19
ask=int(input('Guess my age form 1 to 30:'))
if win==ask:
    print('Right guess')
else:
    if ask>win:
        print('its high')
    else:
        print('its Low')    
