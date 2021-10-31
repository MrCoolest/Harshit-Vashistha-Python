from csv import DictWriter

with open("DictFile.csv",'w',newline='') as f:
    csv_file = DictWriter(f, fieldnames=['Names','Age','Class'])
    csv_file.writeheader()
    # csv_file.writerow(
    #     {'Names' : 'Ankit', 'Age' : 19,'Class' : 'Bsc-it'}
    # )
    # csv_file.writerow(
    #     {'Names' : 'Anuraag', 'Age' : 19,'Class' : 'Bsc-it'}
    # )
    # csv_file.writerow(
    #     {'Names' : 'Dinesh', 'Age' : 19,'Class' : 'Bsc-it'}
    # )
    csv_file.writerows(
        [
            {'Names' : 'Ankit', 'Age' : 19,'Class' : 'Bsc-it'},
            {'Names' : 'Anuraag', 'Age' : 19,'Class' : 'Bsc-it'}
        ]
    )