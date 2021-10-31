# function returning function

def hello1():
    def hi():
        print('Inside is empty')
    return hi

var = hello1()
var() #This is returning inside function (hi)

# 2nd example

def hello2(msg):
    def hii2():
        print(f'Message is {msg}')
    return hii2

var2 = hello2("I'm Ankit")
var2()        

