correct_number = (67)
guess = int(input("enter number: "))
while guess != correct_number:
    if guess < correct_number:
        print("Too low! Try again.")
    elif guess > correct_number:
        print("Too high! Try again.")
    guess = int(input("Enter a number: "))
    print("Congratulations! You've guessed the correct number!")
