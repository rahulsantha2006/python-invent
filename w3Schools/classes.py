# the basics of classes, not really used in real life coding
''' class Myclass:
    x=5

print(Myclass)
p1 = Myclass()
print(p1.x)
'''


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myFunc(self):
        print('Hello my name is ' + self.name)

p1 = Person("Sibi", 12)
p1.age = 100
p1.myFunc()
print(p1.age)

''' there is a del keyword that you can use to delete objects for a class
  this could be written like del p1, or if you wanted to delete a variable: del p1.age'''