#design a faulty calc, which will correctly solve alll the problems except following
#45*4=445, 55+8=348, 54/7=6

print("enter first number")
num1 = int(input())
print("enter second number")
num2 = int(input())
print("choose your choice","+,  /, *, %")
num3 = input()

if num1 == 45 and num2 == 4 and num3 == "*":
    print("445")

elif num1 == 55 and num2 == 8 and num3 == "+":
    print("348")

elif num1 == 54 and num2 == 7 and num3 == "/":
    print("6")

elif num3 == "*":
    num4=num1*num2
    print(num4)

elif num3 == "+":
    plus = num2+num1
    print(plus)

elif num3 == "/":
    div = num2/num1
    print(div)

elif num3 == "%":
    modulo = num2%num1
    print(modulo)

else:
    print("error! check your input")
