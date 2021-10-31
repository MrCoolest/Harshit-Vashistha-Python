# reading one file and writing in another file

with open('new.txt', 'r') as reading:
    with open('coped new file.txt','w') as writing:
        writing.write(reading.read())
