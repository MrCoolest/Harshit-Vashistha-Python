# Functions with all parameters
# very important to understand

# PADK (Parameter, *args, default parameter, kwargs)

def any(name, *args, Age = 19, **kwargs):
    print(name)
    print(args)
    print(Age)
    print(kwargs)

any('ANKIT PATWA', 1,2,3,4, Age=20, Mark = 90, marks = 98)
