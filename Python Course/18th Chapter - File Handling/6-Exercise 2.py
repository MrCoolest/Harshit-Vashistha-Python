with open('links.html', 'r') as rf:
    with open('copy link.txt','w') as wf:
        for line in rf.readlines():
            if 'a href=' in line:
                new = line.find('a href=')
                a = line.find('\"',new)
                b = line.find('\"',a+1)
                url = line[a+1:b]
                wf.write(f'{url} \n')