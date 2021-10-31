# Exeption handling
# try,expect,else, finally

while True:
    try:
        age  = int(input('Enter your age:'))
        break
    except ValueError:
        print('You entered string value, which is not alowed..')
    except:
        print('Unexpected error')


if age > 18:
    print('You can watch this movie !')
else :
    print('You can\'t watch this movei...')    