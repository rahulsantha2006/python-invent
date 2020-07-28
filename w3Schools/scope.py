def firstFunc():
    x = 10
    print(x)
firstFunc()
# variables are not accecible outside the function, but functions inside the function can access the variable
def secondFunc():
    y=20
    def innerFunc():
        print(y)
    innerFunc()

secondFunc()
# there can be a variable with the same name inside a function and outside as a global and private variable

z = 500
def thirdFunc():
    z = 100
    print(z)
thirdFunc()
print(z)
# you can create a variable inside a function and use the global function to make it global

def fourthFunc():
    global a
    a = 10

fourthFunc()
print(a)