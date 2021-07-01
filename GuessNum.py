import random

randomNum = random.randint(0, 10)

while True:
    try:
        userInput = int(input("What number am I thinking of? \n Enter: "))
        while userInput != randomNum:
            if userInput < randomNum:
                userInput = int(input("Try a higher number: "))
            if userInput > randomNum:
                userInput = int(input("Try a lower number: "))
            if userInput == randomNum:
                print("YOU GOT IT!")
                break
    except ValueError:
        print("That is not a number!")
