# Decoraters ---> enhance the funcationality of other function
# @ use for Decoraters 
def Decoraterss(take_function):
    def calling_function():
        print('Hey everyone')
        take_function()
    return calling_function

@Decoraterss
def func1():
    print("I'm Ankit")

def func2():
    print("I'm Coolest")

var = Decoraterss(func1)
var()

var2 = Decoraterss(func2)
var2()

func1()
func2()