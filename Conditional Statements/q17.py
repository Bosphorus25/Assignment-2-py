num = int(input("enter a number: "))
if (num % 2 == 0) and (num % 3 == 0):
    print(num,"is divisible by both 2 and 3")
elif num % 2 == 0:
    print(num,"is divisible by 2 but not by 3")
elif num % 3 == 0:
    print(num,"is divisible by 3 but not by 2")
elif (num % 2 != 0) and (num % 3 != 0): 
    print(num,"non divisible by both 2 and 3")
