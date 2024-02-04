"""i = 0
while(i<49):
    if(i+1<5):
        i = i+1
        continue
    print(i+1, end=" ")
    
    if(i==44):
        break
    i = i+1"""

"""while(True):
    inp = int(input("enter the number"))
    if(inp>100):
        print("congrats you enter the number greater than 100")
        break
    else:
        print("try again")
        continue"""

"""#print the number until multiple of 6 comes"""

"""while(True):
    inp = int(input("enter the number"))
    if(inp % 6 == 0):
        print("yes u got multiple of 6")
        break
    else:
        print("error 404")
        continue"""

"""list = ["sumit", "amit", "sujit", "sujal", "golu", "shinu"]

i = 0
while(True):
    print(list[i])
    if(list[i]=="sumit"):
        print("found the name sumit")
        break
    print("after break statement")
    i += 1
    print("after while loop exit")"""

"""#print table of 5

i = 1
while(True):
    print("5*", (i), "=", 5*i)

    if(i>=10):
        break
    i += 1"""

#print all odd number bw 1 to 50

"""i = 1
while(True):
    for i in range(1, 50, 1):
        if(i % 2 != 0):
            print("odd")
            break
        else:
            print("even")
            continue"""

#print sum of 5 natural number

"""num_sum = 0
count = 0
while(count<10):
    num_sum = num_sum + count
    count = count + 1
    if(count==5):
        break
    print("sum of first", count, "integer is :", num_sum)"""

#print word of python

"""for letter in "python":
    if letter == "h":
        continue
    print("current letter")

var = 10
while(var>0):
    var = var-1
    if var ==5:
        continue
    print("current variable value", var)
    print("good bye")"""

#print all letter of ur choice and end

"""for char in "sumit":
    if char == "t":
        break
    print(char)

print("end")"""

"""for i in range(10):
    print(i)
    if(i==7):
        print("break")
        break"""


#print number and when comes more than 100 break
"""i = 0
while(True):
    inp = int(input("enter the number"))
    if(i>100):
        break
    print("number", i)
else:
    print("stop")"""


#print the square of any number

number = [2, 3, 7, 11]
for i in number:
    print("current number is", i)
    if(i>10):
        continue
    square = i * i
    print("square of a current number is", square)