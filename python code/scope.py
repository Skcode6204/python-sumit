#scope : global variable & local variable

"""l = 15   #global variable

def function1(n):
    l = 6  #local variable
    m = 9   #local variable
    print(l, m)
    print(n, "I am sumit")
    
function1("This is me")"""

"""l = 15   #global variable

def function1(n):
    #l = 6  #local variable
    m = 9   #local variable
    print(l, m)
    print(n, "I am sumit")
    
function1("This is me")"""

#changing of global variable

"""l = 15   #global variable

def function1(n):
    #l = 6  #local variable
    m = 9   #local variable
    global l
    l = l + 45
    print(l, m)
    print(n, "I am sumit")
    
function1("This is me")"""


#global variable

x = 91
def sumit():
    x = 20
    def sujit():
        global x 
        #x = 87
    print("before calling sujit()", x)
    sujit()
    print("after calling sujit()", x)

sumit()
print(x)

        



