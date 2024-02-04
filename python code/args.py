"""def function_name_print(a, b, c, d, e):
    print(a, b, c, d, e)


function_name_print("sumit", "amit", "sujit", "shinu", "guddu")"""

#we cant add more name therefore to overcome this problem we use args and kwargs function

#args

def funargs(normal*args):
    var = ["sumit", "amit", "sujit"]
    funargs(*var)