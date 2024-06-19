num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
str = input("Enter operand(+,-,*,/,%): ")
if str == "+":
    print(num1+num2)
elif str == "-":
    print(num1-num2)
elif str == "*":
    print(num1*num2)
elif str == "/":
    print(num1/num2)
elif str == "%":
    print((num1%num2))