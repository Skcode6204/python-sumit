#lists in python

grocery = ["rice", "pulses", "oil", "onion", "potato", "vimbar"]
print(grocery)

print(grocery[3])

numbers = [2, 5, 4, 7, 9]
print(numbers[2])

numbers.sort()
print(numbers)

numbers.sort()
numbers.reverse()
print(numbers)

numbers.append(31)
numbers.append(37)
numbers.append(361)
print(numbers)

numbers.insert(2, 64)
print(numbers)

numbers.remove(5)
print(numbers)

numbers.pop()
print(numbers)

numbers[1] = 89
print(numbers)

#mutable - can change
#inmutable - cannot change

tp = (1,4,7)
print(tp)

#swap any two numbers

a = 1
b = 5
temp = a
a = b
b = temp
print(a, b)

x = 4
y = 8
x, y = y, x
print(x, y)
