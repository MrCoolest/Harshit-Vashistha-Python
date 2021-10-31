a=input('Enter your name:')
temp=''
for i in range(len(a)):
    if a[i] not in temp:

        temp+=a[i]
        print(f'{a[i]}:{a.count(a[i])}')