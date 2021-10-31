import mysql.connector

conn = mysql.connector.connect(host="localhost", username="root", password='bhagwan', database="new_db")

My_cursor = conn.cursor()

# query = "CREATE DATABASE new_DB"

# query = "SHOW DATABASES"

# My_cursor.execute("CREATE TABLE Student(name VARCHAR(20), age INT)")

# query = "INSERT INTO student(name, age) VALUES(%s, %s)"
# val = ("Ankit",19)

val = [
    ("Bhagwan", 23),
    ("AYsh", 20),
    ("PArth", 345),
    ("helk", 29),
    ("Captian", 900),
    ("MArvel", 567)
]
# My_cursor.execute(query, val)
# My_cursor.executemany(query, val)


query = "SELECT * FROM student"

My_cursor.execute(query)


for row in My_cursor:
    print(row)


# for db in My_cursor:
#     print(db)


# print(My_cursor.fetchall())
conn.commit()
conn.close()

# print