import time

"""initial = time.time()

k=0                                            #this program show that speed of while loop and for loop are almost same
while(k<40):
    print("my name is sumit")
    k+=1
print("while loop ran in", time.time() - initial, "seconds")

initial2 = time.time()

for i in range(40):
    print("my name is sumit")
print("for loop ran in", time.time() - initial2, "seconds")"""

localtime = time.asctime(time.localtime(time.time()))
print(localtime)
