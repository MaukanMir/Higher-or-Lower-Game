import random

def welcome_message():
    print("Welcome to the guessing game!")

welcome_message()
difficulty = input("Choose the level of difficulty: Easy or Hard?: ").lower()

def amount_of_lives(difficulty):
    if difficulty == 'easy':
        return 10
    else:
        return 5

guess = int(input("Guess a number between 1 and 100: "))
computers_pick = random.randint(1, 100)

lives = amount_of_lives(difficulty)
def continue_game(guess,computers_pick,lives):
    if guess > computers_pick:
        lives -= 1
        if lives >= 1:
            print("Sorry that is too high")
            print(f"You have {lives} lives left")
        else:
            if lives < 1:
                return True
    elif guess < computers_pick:
        lives -= 1
        if lives >= 1:
            print("Sorry that is too low")
            print(f"You have {lives} lives left")
        else:
            if lives < 1:
                return True

    elif computers_pick == guess:
        print(f"Congrats you won the game with {lives} lives remaining")
        return True


def main(guess,computers_pick,lives):
    while not continue_game(guess,computers_pick,lives):
        guess = int(input("Guess a number between 1 and 100: "))
        lives-=1
    else:
        play_again = input("Game Over. Would you like to play again? Enter 'y' or 'n': ").lower()
        if play_again == 'y':
            difficulty = input(
                "Choose the level of difficulty: Easy or Hard?: ").lower()
            amount_of_lives(difficulty)
            lives = amount_of_lives(difficulty)
            computers_pick = random.randint(1, 100)
            guess = int(input("Guess a number between 1 and 100: "))
            main(guess,computers_pick,lives)
        else:
            if play_again == 'n':
                print("See you next time!")
            

main(guess,computers_pick,lives)


    
