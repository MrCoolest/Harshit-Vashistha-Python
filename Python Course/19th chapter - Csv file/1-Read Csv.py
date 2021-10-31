from csv import reader

with open('file.csv', 'r') as r_f:
    csv_file = reader(r_f)
    # csv_file is iterator
    for rows in csv_file:
        print(rows)