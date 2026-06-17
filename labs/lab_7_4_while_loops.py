# Devin Thomas
# Jun 1, 2024

from random import randint


def main() -> None:
    correct_answer: int = randint(1, 100)
    attempts: int = 0
    user_guess: int = 0
    while user_guess != correct_answer:
        attempts += 1
        user_guess = int(input(f"Attempt {attempts}: Try to guess the correct number from 1-100: "))
    print(f"You found it! The number was {correct_answer}.")


if __name__ == '__main__':
    main()
