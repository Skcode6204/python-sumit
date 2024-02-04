#write anything on file

"""f = open("sumit2.txt", "w")
content = f.write("sumit is a very good boy")
print(content)
f.close()"""

#append (add) anything on file

"""f = open("sumit2.txt", "a")
a = f.write("sumit is a intelligent boy\n")
print(a)
f.close()"""

#handle write and read both
f = open("sumit2.txt", "r+")
print(f.read())
f.write("thank you")
f.close()
