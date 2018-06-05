class Computer:

    def __init__(self, ram, memory, processor):
        self.ram = ram
        self.memory = memory
        self.processor = processor

    def getspecs(self):
        print('Enter the details')
        self.ram = input('enter the value of ram')
        self.memory = input('enter the value of memory')
        self.processor = input('enter the value of processor')

    def displayspecs(self):
        print('display the specification')
        print('ram size is:' + self.ram + " " + 'MB' + 'memory size is:' + " " + 'HZ' + self.memory + " " + 'processor size is:'+self.processor)


comp = Computer("blank", 0, 0);
comp.getspecs()
comp.displayspecs()

class Display(Computer):

    def __init__(self, color):
        self.color = color

    def getspecs(self):
        self.color = input('enter the color')

    def displayspecs(self):
        print('the color is :' + self.color)

dis = Display('blank')
dis.getspecs()
dis.displayspecs()


class Laptop(Computer):

    def __init__(self, weight):
        self.weight = weight

    def getspecs(self):
        self.weight = input('weight is')

    def displayspecs(self):
        print('weight is :' + self.weight + " " + 'kg')

lap = Laptop('blank');
lap.getspecs()
lap.displayspecs()



