with open('Exercise 1 text.txt','r') as re:
    with open('Copy From Exercise 1.txt', 'w') as rw:
        for i in re.readlines():
            name, salary = i.split(',')
            rw.write(f'{name}\'s salary is {salary}')
