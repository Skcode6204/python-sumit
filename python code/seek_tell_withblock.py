#use of seek() & tell()

"""f = open("sumit2.txt")
f.seek(11)
print(f.tell())
#print(f.readline())
print(f.readlines())"""


#use of with_block

with open("sumit2.txt") as f:
    a = f.readlines()
    print(a)
