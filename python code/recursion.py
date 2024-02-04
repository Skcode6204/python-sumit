#find factorial using iteration and recursison method
#factorial = n! = n * n-1 * n-2 * n-3 *.........1
#n! = n * (n-1)!

#factorial by iteration
"""def factorial_iterative(n):
    
    #:parameter n = integer
    #:return = n * n-1 * n-2 * n-3 *.........1 

    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac

number = int(input("enter the number"))
print(factorial_iterative(number))"""

#factorial by recursion
"""def factorial_recursive(n):
    #:parameter n = integer
    #:return = n * n-1 * n-2 * n-3 *.........1 

    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)

number = int(input("enter the number"))
print(factorial_recursive(number))"""

#wap to print fibonacci sequence
#fibonacci = 0,1,1,2,3,5,8,13,........

def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

number = int(input("enter the number"))
print(fib(number))
    





    




