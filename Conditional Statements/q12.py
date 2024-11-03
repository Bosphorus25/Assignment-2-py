num = int(input("Degree Celcius: "))
if num > 14 and num < 33:
    print(num,"its Moderate")
elif num <= 14:
    print(num,"its Cold")
else:
    print(num,"its Hot")