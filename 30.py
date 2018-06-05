# object oriented programming

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

john = students("blank", 0)
john.getdata()
john.putdata()
