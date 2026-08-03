import random
import function

print("=== NUMBER GUESSING GAME ===\n\nI'm thinking of a number between 1 and 100.\n")

print("""Easy mode grants you 10 attempts, normal mode grants you 7 attempts, hard mode grants you 5 attempts.
Enter 1 to choose easy mode, 2 to choose normal mode and 3 to choose hard mode!""")

hardness = function.chooseHardness()

number = random.randint(1, 100)

win = lose = False

attempts = 0

playing = True

guessedNumbers = []

while playing:
    try:
        if attempts < hardness:
            guess = int(input("Your guess: "))
            if guess in guessedNumbers:
                print("You already guessed this number!")
                continue    
            if 1 <= guess <= 100:
                guessedNumbers.append(guess)
                attempts+=1
                if guess == number:
                    print(f"\nCorrect!\nYou won in {attempts} attempt" if attempts == 1 else f"\nCorrect!\nYou won in {attempts} attempts")
                    win = True
                elif guess > number:
                    print("The number is lower!\n")
                    print(f"You have {hardness-attempts} attempt left!\n" if hardness-attempts <= 1 else f"You have {hardness-attempts} attempts left!\n")
                else:
                    print("The number is higher!\n")
                    print(f"You have {hardness-attempts} attempt left!\n" if hardness-attempts <= 1 else f"You have {hardness-attempts} attempts left!\n")
            else:
                print("Please enter an integer between 1 and 100!")
        else:
            print(f"GAME OVER!\nThe number is {number}")
            lose = True
        while lose or win:
            playAgain = input("Do you want to play again? y/n ")
            if playAgain.lower() == "y":
                hardness = function.chooseHardness()
                number = random.randint(1, 100)
                win = lose = False
                attempts = 0
                guessedNumbers = []
            elif playAgain.lower() == "n":
                playing = False
                break
            else:
                print("Please enter y or n!")    

    except ValueError:
        print("Please enter an integer between 1 and 100!")
