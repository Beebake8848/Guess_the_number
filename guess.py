import random as rd

while True:
    x = rd.randint(1, 10)
    score = 10
    attempts = 1

    while True:
        y = int(input("Enter a number: "))

        if y == x:
            print("Congratulations! Your guess is correct.")
            break
        else:
            score -= 1
            attempts += 1
            print("Try again.")

    print("Number of attempts: {} | Your score is {}".format(attempts, score))

    choice = input("Do you want to play again? (yes/no): ")
    if choice.lower() != "yes":
        break
