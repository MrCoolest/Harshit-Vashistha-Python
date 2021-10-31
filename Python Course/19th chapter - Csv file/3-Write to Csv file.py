# writer, DictWriter
from csv import writer

with open('File2.csv','w',newline='') as wf:
    # methods = 
    csv_file = writer(wf)
    # csv_file.writerow(['Name','age'])
    # csv_file.writerow(['Ankit','19'])
    # csv_file.writerow(['Yash','20'])
    # csv_file.writerow(['Raj','21'])

    csv_file.writerows([['Name','Age','say'],['Ankit',19,'Hii'],['Yash',20,'hello']])
