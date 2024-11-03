print("enter triangle sides one by one")
a = int(input("enter side 1: "))
b = int(input("enter side 2: "))
c = int(input("enter side 3: "))
if (a == b == c):
    print(a,b,c,"is a Equilateral Triangle")
elif (a == b) or (b == c) or (c == a):
    print(a,b,c,"is a Isosceles Triangle")
elif (a != b) or (b != c) or (c != a):
    print(a,b,c,"is a Scalene Triangle")

#Equilateral Triangle: All three sides are of equal length, and all three angles are also equal (each measuring 60 degrees).

#Isosceles Triangle: Two sides are of equal length, and the angles opposite those sides are also equal.

#Scalene Triangle: All three sides are of different lengths, and all three angles are different as well.