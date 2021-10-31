ask=input('Enter any number more than 1 digit:')  
total=0
i=0
while i < len(ask):
    total+=int(ask[i])
    i+=1 
print(total)    