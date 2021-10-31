# Exercise Question 4: Create a function showEmployee() in such a way that it should accept employee 
# name, and it’s salary and display both, and if the salary is missing in function call it should 
# show it as 9000

def showEmployee(name,salary = 9000):
    print(f"i'm {name}, and my salary is {salary}")

showEmployee('Ankit patwa',30000)
showEmployee("Ankit")
