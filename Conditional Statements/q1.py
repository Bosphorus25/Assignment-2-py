age = int(input("enter your age: "))
if age < 18:
    print(age,"you are minor.")
elif age <= 50 and age >= 18:
    print(age,"you are adult.")
else:
    print(age,"you are senior citizen.")