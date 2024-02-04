s = set()
print(type(s))

s1 = set([1,3,5,7])
print(s1)

s1.add(4)
print(s1)

s1.remove(3)
print(s1)

s2 = s1.union([9, 8])
print(s, s2)

s2 = s1.intersection([7, 8])
print(s2)

