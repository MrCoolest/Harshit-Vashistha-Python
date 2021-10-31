# VARIABLE SCOPE

x=40   #this is global variable

def vari():
    global x #it is changing global variable But it give as again global value before def
    x=70       #this is local variable
    return x

print(x) #this is global value
print(vari())
print(x)  #this is changed value