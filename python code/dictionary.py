#uses of dictionary in python

d1 = {}
print(type(d1))

d1 = {"my name is sumit"}
print(d1)

d2 = {"sumit" : "chicken", "amit" : "fish", "sujeet" : "mutton", "shinu" : "biscuits",
 "guddu" : {"B" : "roti", "L" : "chawal", "D" : "chicken"}}
d2["sujal"] = "junk food"
d2["babu"] = "magggie"
del d2["sujal"]
print(d2) 

print(d2["sujeet"])
print(d2["guddu"])
print(d2["guddu"]["L"])

print(d2.copy())

d3 = d2
print(d3)

del  d3["amit"]

d2.update({"anjali" : "pasta"})
print(d2)

print(d2.keys())
print(d2.items())







