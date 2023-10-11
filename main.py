import random


def play_again():
    play_again = input("Do you want to play again? (yes/no) ").lower()
    return play_again.startswith('y')


def choose_difficulty():
    difficulties = {
        'easy': (1, 50),
        'medium': (1, 100),
        'hard': (1, 200)
    }

    print("Choose a difficulty level:")
    for level, (low, high) in difficulties.items():
        print(f"{level.capitalize()} ({low}-{high})")
    
    while True:
        choice = input('Enter your choice of difficulty: ').strip().lower()
        if choice in difficulties:
            return difficulties[choice]
        print('Invalid choice. Please try again.')


def take_guess(low, high):
    while True:
        guess = input(f'Enter your guess ({low}-{high}): ')
        if guess.isdecimal():
            guess = int(guess)
            if low <= guess <= high:
                return guess
        print(f'Please enter a valid number between {low} and {high}.')

def display_welcome_message():
    print(f'Hello, {myName}! Welcome to the Guessing Game!')

def display_result_message(guess_taken):
    if guess_taken == 1:
        print(f'Wow, {myName}! You guessed my number in 1 try! You\'re a genius!')
    else:
         print(f'Good job, {myName}! You guessed my number in {guess_taken} tries!')

def main_game_loop():
    score = 10
    while True:
        low, high = choose_difficulty()
        secret_number = random.randint(low, high)

        print(f'I am thinking of a number between {low} and {high}')

        for guess_taken in range(10):
            print(f'You have {10 - guess_taken} guesses left.')
            guess = take_guess(low, high)

            if guess == secret_number:
                break
            elif guess < secret_number:
                print('Your guess is too low.')
            else:
                print('Your guess is too high')

        else:
            print(f'Game Over! The number I was thinking of was {secret_number}.')

        if guess == secret_number and guess_taken < score:
            display_result_message(guess_taken+1)
            score -= (guess_taken+1)
        else:
            print(f'Game Over! The number I was thinking of was {secret_number}.')  

        print(f'Your Score: {score}')

        if not play_again():
            print(f'Thank you for playing, {myName}!')
            break


# Entry Point
print('Hello! What is your name?')
myName = input('>')
myName = myName.title()
display_welcome_message()
main_game_loop()
