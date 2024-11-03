num = int(input("enter number 1: "))
num1 = int(input("enter a number 2: "))
num2 = input("enter operator: ")
if num2 == "+":
    print(num + num1)
elif num2 == "-":
    print(num - num1)
elif num2 == "*":
    print(num * num1)
elif num2 == "/":
    print(num / num1)
else:
    print("Error")

