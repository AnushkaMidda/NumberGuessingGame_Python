# Path: Number_Guessing_Game/game.py

import random
import os
from datetime import datetime

try:
    from colorama import init, Fore, Style
    init(autoreset=True)
except ImportError:
    # If colorama is not installed, define dummy colors
    class Fore:
        RED = ''
        GREEN = ''
        YELLOW = ''
        CYAN = ''
    class Style:
        BRIGHT = ''
        RESET_ALL = ''

# --- Welcome and Player Name ---
print(Fore.CYAN + Style.BRIGHT + "🎉 Welcome to the Number Guessing Game! 🎉\n")
player_name = input("Enter your name: ").strip() or "Player"

print(f"\nHello {player_name}! Here are the rules:")
print("1. Select difficulty: Easy / Medium / Hard / Custom range")
print("2. Try to guess the number randomly chosen by the computer")
print("3. You will get feedback if your guess is too low or too high")
print("4. Your attempts will be counted\n")

# --- Difficulty selection ---
def select_difficulty():
    print("Select Difficulty Level:")
    print("1. Easy (1-20)")
    print("2. Medium (1-60)")
    print("3. Hard (1-120)")
    print("4. Custom Range")
    
    while True:
        choice = input("Enter your choice (1-4): ").strip()
        if choice == '1':
            return 1, 20
        elif choice == '2':
            return 1, 60
        elif choice == '3':
            return 1, 120
        elif choice == '4':
            while True:
                try:
                    min_val = int(input("Enter minimum number (>=0): "))
                    max_val = int(input("Enter maximum number (<=10000): "))
                    if min_val >= max_val:
                        print(Fore.RED + "Minimum should be less than maximum. Try again.")
                    else:
                        return min_val, max_val
                except ValueError:
                    print(Fore.RED + "Please enter valid integers.")
        else:
            print(Fore.RED + "Invalid choice. Please enter 1, 2, 3, or 4.")

min_num, max_num = select_difficulty()
print(Fore.YELLOW + f"\nYou selected range: {min_num} to {max_num}\n")

# --- Random number generation ---
number_to_guess = random.randint(min_num, max_num)
attempts = 0

# --- Main Game Loop ---
while True:
    try:
        guess = int(input(f"Enter your guess ({min_num}-{max_num}): "))
        attempts += 1

        if guess < number_to_guess:
            print(Fore.RED + "Please guess higher!\n")
        elif guess > number_to_guess:
            print(Fore.RED + "Please guess lower!\n")
        else:
            print(Fore.GREEN + Style.BRIGHT + f"🎉 Correct! You guessed the number in {attempts} attempts.\n")
            break
    except ValueError:
        print(Fore.RED + "Invalid input! Please enter a number.\n")

# --- Best Score Tracking ---
BEST_SCORE_FILE = "best_score.txt"

def read_best_score():
    if os.path.exists(BEST_SCORE_FILE):
        with open(BEST_SCORE_FILE, "r") as file:
            try:
                score, date_str = file.read().split(",")
                return int(score), date_str
            except:
                return None, None
    return None, None

def write_best_score(score):
    with open(BEST_SCORE_FILE, "w") as file:
        file.write(f"{score},{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

best_score, best_date = read_best_score()
if best_score is None or attempts < best_score:
    print(Fore.CYAN + f"🎯 New Best Score! You guessed in {attempts} attempts.")
    write_best_score(attempts)
else:
    print(Fore.CYAN + f"Your attempts: {attempts}. Best Score so far: {best_score} attempts on {best_date}")

# --- Replay Option ---
while True:
    replay = input("\nDo you want to play again? (Y/N): ").strip().upper()
    if replay == 'Y':
        print("\nRestarting game...\n")
        import sys
        python = sys.executable
        os.execl(python, python, * sys.argv)
    elif replay == 'N':
        print(Fore.YELLOW + f"Thanks for playing, {player_name}! Goodbye! 🎉")
        break
    else:
        print(Fore.RED + "Please enter Y or N.")
