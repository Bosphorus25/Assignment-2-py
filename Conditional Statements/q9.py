print("enter triangle sides one by one")
a = int(input("enter side 1: "))
b = int(input("enter side 2: "))
c = int(input("enter side 3: "))
if (a + b > c) and (a + c >b) and (b + c > a):
    print(a,b,c,"is a valid triangle")
else:
    print(a,b,c,"is not a valid triangle")