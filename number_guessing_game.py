print("Welcome to the guessing game")
secret=27
for i in range(5):
    guess=int(input("Guess a number between 1-100 and you get 5 attempts"))
    if guess==secret:
        print("You guessed it")
        print("You won the game")
        break
    else:
        if guess<=27+5 and guess>=27-5:
            print("Hot")
        elif guess<=27+10 and guess>=27-10:
            print("Warm")
        elif guess<=27+25 and guess>=27-25:
            print("Cold")
        else:
            print("Ice Cold")
print("Game over")