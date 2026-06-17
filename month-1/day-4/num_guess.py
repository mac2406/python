secret_number = 7

while True:
    guess = int(input("Guess the number: "))
    if guess == secret_number:
        print("Congratulations!")
        break
    else:
        print("Try Again")
