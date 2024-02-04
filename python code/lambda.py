#lambda function and  anonymous function

"""def add(a, b):
    return a + b"""

#in place of def function we can use the lambda function 


#add = lambda x, y: x + y

"""def minus(a, b):
    return a - b
print(minus(8, 5))"""

"""minus = lambda a, b: a - b
print(minus(9, 4))"""

a = [[1, 12], [5, 6], [8, 23]]
a.sort(key = lambda x:x[1])
print(a)
