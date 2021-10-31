# reader, dictreader
# writer, dictwriter

from csv import DictReader, DictWriter

with open('DictFile.csv','r') as rf:
    with open('NewDict.csv','w',newline='') as wf:
        csv_read = DictReader(rf)
        csv_write = DictWriter(wf,fieldnames=['Name','Age','Class','say'])
        csv_write.writeheader()
        for row in csv_read:
            a,b,c =row['Names'],row['Age'], row['Class']
            csv_write.writerow({
                'Name' : a.title(),
                'Age' : b,
                'Class' : c,
                'say' : 'Hii'
            })