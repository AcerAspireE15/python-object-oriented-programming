class number:

    def __init__(self, x):
        self.x = x

    def __mul__(self, other):
        x = self.x + other.x
        return x

number_a = number(3)
number_b = number(4)

print(number_a * number_b)
