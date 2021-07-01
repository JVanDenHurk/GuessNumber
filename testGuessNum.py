import random

diffInput = input(
    "Choose your difficulty. easy(e), medium(m) or hard(h)?").lower()

if diffInput == "easy" or "e":

    randomNum = random.randint(0, 10)

    while True:

        try:
            userInput = int(input("What number am I thinking of? \n Enter: "))
            break
        except ValueError:
            print("That is not a number!")

    while userInput != randomNum:

        if userInput < randomNum:

            print("Try a higher number")
            userInput = int(input())

        if userInput > randomNum:

            print("Try a lower number")
            userInput = int(input())

        if userInput == randomNum:
            print("YOU GOT IT!")

elif diffInput == "medium" or "m":
    # randomNum = random.randint(0, 100)

    print("Loading.....")

elif diffInput == "hard" or "h":
    #randomNum = random.randint(0, 1000)
    print("Loading... V2")

elif diffInput != "easy" or "e" or "medium" or "m" or "hard" or "h":
    userInput = input(
        "Please choose a difficulty. easy(e), medium(m) or hard(h)?").lower()
