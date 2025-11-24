import random

def generate_secret():
    """
    Generate a 4-digit secret number with all different digits.
    Returns a string like '2153'.
    """
    digits = list("0123456789")
    random.shuffle(digits)
    return "".join(digits[:4])


def check_guess(secret: str, guess: str):
    """
    Compare guess to secret and return feedback.
    '*' = correct digit in correct place
    '+' = correct digit wrong place
    """
    stars = 0
    pluses = 0

    for i in range(4):
        if guess[i] == secret[i]:
            stars += 1
        elif guess[i] in secret:
            pluses += 1

    return "*" * stars + "+" * pluses


def play():
    """
    Command-line game loop.
    """
    secret = generate_secret()
    attempts = 0

    print("Welcome to MasterMind!")
    print("Guess the 4-digit number (all digits different).")

    while True:
        guess = input("Your guess: ").strip()
        attempts += 1

        # basic validation
        if len(guess) != 4 or not guess.isdigit() or len(set(guess)) != 4:
            print("Invalid guess. Must be 4 different digits.")
            continue

        response = check_guess(secret, guess)
        print("Response:", response)

        if response == "****":
            print(f"Correct! The number was {secret}. Attempts: {attempts}")
            break


if __name__ == "__main__":
    play()
