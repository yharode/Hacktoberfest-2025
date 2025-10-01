import random

def get_valid_number(prompt: str) -> int:
    """Prompt user until a valid integer is entered."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")

def play_game():
    print("🎮 Welcome to the Number Guessing Game!")
    print("I have picked a number between 1 and 100. Can you guess it?")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = get_valid_number("Enter your guess: ")
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
            break

if __name__ == "__main__":
    play_game()
