import random
import tkinter as tk
from tkinter import messagebox, simpledialog

def play_again():
    """Ask the user if they want to play again and return the answer."""
    answer = messagebox.askyesno("Play Again", "Do you want to play again?")
    return answer

def choose_difficulty():
    """Display a window to allow the user to choose the difficulty level.
    
    Returns:
        tuple: A tuple representing the chosen difficulty level range.
    """
    difficulties = {
        'easy': (1, 50),
        'medium': (1, 100),
        'hard': (1, 200)
    }

    choice = None

    def set_difficulty(diff):
        """Set the chosen difficulty level."""
        nonlocal choice
        choice = diff
        window.destroy()

    window = tk.Tk()
    window.title("Choose Difficulty")

    for level, (low, high) in difficulties.items():
        btn = tk.Button(window, text=f"{level.capitalize()} ({low}-{high})", command=lambda l=low, h=high: set_difficulty((l, h)))
        btn.pack(pady=5)

    window.mainloop()

    return choice

def take_guess(low, high):
    """Prompt the user to input a guess within the given range.
    
    Args:
        low (int): The lower bound of the valid guess range.
        high (int): The upper bound of the valid guess range.
    
    Returns:
        int: The user's guess.
    """
    guess = tk.simpledialog.askinteger("Guess", f"Enter your guess ({low}-{high}):", minvalue=low, maxvalue=high)
    return guess

def display_welcome_message():
    """Display a welcome message to the user."""
    messagebox.showinfo("Welcome", f"Hello, {myName}! Welcome to the Guessing Game!")

def display_result_message(guess_taken):
    """Display a message based on the user's performance.
    
    Args:
        guess_taken (int): The number of guesses the user took to find the correct answer.
    """
    if guess_taken == 1:
        messagebox.showinfo("Congratulations!", f'Wow, {myName}! You guessed my number in 1 try! You\'re a genius!')
    else:
        messagebox.showinfo("Congratulations!", f'Good job, {myName}! You guessed my number in {guess_taken} tries!')

def main_game_loop():
    """Run the main game loop."""
    score = 10
    while True:
        difficulty = choose_difficulty()
        low, high = difficulty
        secret_number = random.randint(low, high)

        messagebox.showinfo("Game Start", f'I am thinking of a number between {low} and {high}')

        for guess_taken in range(10):
            remaining_guesses = 10 - guess_taken
            guess = take_guess(low, high)

            if guess == secret_number:
                break
            elif guess < secret_number:
                messagebox.showinfo("Hint", 'Your guess is too low.')
            else:
                messagebox.showinfo("Hint", 'Your guess is too high')

        else:
            messagebox.showinfo("Game Over", f'Game Over! The number I was thinking of was {secret_number}.')

        if guess == secret_number and guess_taken < score:
            display_result_message(guess_taken + 1)
            score -= (guess_taken + 1)
        else:
            messagebox.showinfo("Game Over", f'Game Over! The number I was thinking of was {secret_number}.')

        messagebox.showinfo("Your Score", f'Your Score: {score}')

        if not play_again():
            messagebox.showinfo("Goodbye", f'Thank you for playing, {myName}!')
            break

myName = tk.simpledialog.askstring("Name", "Hello! What is your name?")
myName = myName.title()
display_welcome_message()
main_game_loop()
