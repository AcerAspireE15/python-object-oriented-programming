# inheritance in python

class students:

    def __init__(self, name, contact):
        self.name = name
        self.contact = contact


    def getdata(self):
        print('Accepting data')
        self.name = input('Enter name')
        self.contact = input('Enter contact')

    def putdata(self):
        print('the name is:'+self.name, 'this is the contact:'+self.contact)

class ScienceStudent(students):

    def __init__(self,age):
        self.age = age

    def science(self):
        print('i am a science student')

rob = ScienceStudent(20)
rob.science()
rob.getdata()
rob.putdata()
