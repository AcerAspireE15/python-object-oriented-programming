# sets in python

numbers = {1, 2, 3, 4, 5, 6}
print(numbers)
print(5 in numbers)
print(10 in numbers)
numbers.add(9)
print(numbers)
numbers.remove(3)
print(numbers)


seta = {1, 2, 3, 4, 5}
setb = {4, 5, 6, 7, 8}

print(seta  |  setb) # union

print(seta  &  setb) #intersection

print(seta  - setb) #difference
