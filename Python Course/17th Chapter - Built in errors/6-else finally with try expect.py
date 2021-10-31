# else and finally clause in exeption handling
while True:
    try :
        age = int(input('Enter the age:'))
    except ValueError:
        print('You enters wrong input')
    except:
        print('Unexpected error')
    else:
        print('Here is breaking')
        break
    finally:
        print('Finally block.....')     


