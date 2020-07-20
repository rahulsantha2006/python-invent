
class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname(self):
        print(self.firstname, self.lastname)



class Child(Person):

    def Title(self):
        print(" The son of "+a.firstname+ a.lastname+' is , '+b.firstname+b.lastname)

a = Person('Santha', "Perian")
a.printname()

b = Child('Sibi','Santha')
b.printname()
b.Title()