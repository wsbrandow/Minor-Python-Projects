from random import randint

# Random Number Generator/Guessing Game
random_number = randint(1, 10)


while guesses_left > 0:
    guesses_left = 3
    guess = int(raw_input("Your guess: "))
    if guess == random_number:
        print("You win!")
        break
    else:
        
        if guess != random_number:
            print("Nope")
            guesses_left -= guesses_left - 1
            return(guesses_left)
            
        else guesses_left == 0:
            print "You lose"
                        

