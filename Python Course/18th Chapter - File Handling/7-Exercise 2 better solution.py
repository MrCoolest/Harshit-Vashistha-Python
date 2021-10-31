with open('links.html', 'r') as rf:
    with open('new link.txt', 'a') as rw:
        page = rf.read()
        lines_exist = True
        while lines_exist:
            f = page.find('a href=')
            if f == -1:
                lines_exist = False
            else:
                first = page.find('\"',f)
                second = page.find('\"',first+1)
                url = page[first+1:second]
                rw.write(f'{url}\n')
                page = page[second:]