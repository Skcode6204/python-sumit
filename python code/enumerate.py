l1 = ["sumit", "amit", "sujit", "shinu"]

"""i = 1
for item in l1:
    if i%2 !=0:
        print(f"my name is {item}")
    i += 1"""

#in place of this complex program we use enumerate 

for index, item in enumerate(l1):
    if index%2==0:
        print(f"my name is {item}")


