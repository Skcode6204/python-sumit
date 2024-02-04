#Health Management System
#client = Sumit, Amit, Sujit

def getdate():
    import datetime
    return datetime.datetime.now()

#Total 6 files
#write a function that when executed takes as input client name
#write a function that retrieve exercise and food for any client

#here is the program

import datetime
def gettime():
    return datetime.datetime.now()

def take(k):
    if k == 1:
        c = int(input("enter 1 for exercise and 2 for food"))
        if(c == 1):
            value=input("type here\n")
            with open("sumit-ex.txt", "a") as f:
                f.write(str[str(gettime())])+": "+value+"\n"
            print("succesfully written")
        elif(c == 2):
            value = input("type here\n")
            with open("sumit-food.txt", "a") as f:
                f.write(str[str(gettime())])+": "+value+"\n"
            print("succesfully written")

    elif(k == 2):
        c = int(input("enter 1 for exercise and 2 for food"))
        if(c == 1):
            value = input("type here\n")
            with open("amit-ex.txt", "a") as f:
                f.write(str[str(gettime())])+": "+value+"\n"
            print("succesfully written")
        elif(c == 2):
            value = input("type here\n")
            with open("amit-food.txt", "a") as f:
                f.write(str[str(gettime())])+": "+value+"\n"
            print("succesfully written")

    elif(k == 3):
        c = int(input("enter 1 for exercise and 2 for food"))
        if(c == 1):
            value = input("type here\n")
            with open("sujit-ex.txt", "a") as f:
                f.write(str[str(gettime())])+": "+value+"\n"
            print("succesfully written")
        elif(c == 2):
            value = input("type here\n")
            with open("sujit-food.txt", "a") as f:
                f.write(str[str(gettime())])+": "+value+"\n"
            print("succesfuly written")

    else:
        print("plz enter valid input (1(sumit), 2(amit), 3(sujit)")

def retrieve(k):
    if k == 1:
        c = int(input("enter 1 for exercise and 2 for food"))
        if(c == 1):
            with open("sumit-ex.txt") as f:
                for i in f:
                    print(i, end = "")
        elif(c == 2):
            with open("sumit-food.txt") as f:
                for i in f:
                    print(i, end = "")

    elif k == 2:
        c = int(input("enter 1 for exercise and 2 for food"))
        if(c == 1):
            with open("amit-ex.txt") as f:
                for i in f:
                    print(i, end = "")
        elif(c == 2):
            with open("amit-food.txt") as f:
                for i in f:
                    print(i, end = "")

    elif k == 3:
        c = int(input("enter 1 for exercise and 2 for food"))
        if(c == 1):
            with open("sujit-ex.txt") as f:
                for i in f:
                    print(i, end = "")
        elif(c == 2):
            with open("sujit-food.txt") as f:
                for i in f:
                    print(i, end = "")

    else:
        print("plz enter valid input(sumit, amit, sujit)")
print("health management system: ")
a = int(input("press 1 for log the value and 2 for retrieve "))

if a == 1:
    b = int(input("press 1 for sumit 2 for amit 3 for sujit"))
    take(b)

else:
    b = int(input("press 1 for sumit 2 for amit 3 for sujit "))
    retrieve(b)








