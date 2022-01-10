import random


def guessing_game():
    n = random.randint(1, 100)
    counter = 1
    print("Please enter an integer: ", end="")
    input_integer = int(input())
    while input_integer != n:
        counter += 1
        if input_integer < n:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
        print("Please enter an integer again: ", end="")
        input_integer = int(input())
    print("Congratulations! You take {} guesses to reach the correct answer.".format(counter))


def reversed_guessing_game():
    interval_a = 1
    interval_b = 101
    guess = (interval_a + interval_b) // 2
    print(
        "Please choose a secret number in the interval [1,100].Then enter one of L (if the guess was lower than the secret number), H (if the guess was higher than the secret number) or C (if the guess was correct).")
    while True:
        print("The secret number is {}. Is it right?".format(guess))
        print("Please enter one of L, H, or C: ", end="")
        input_symbol = input()
        if input_symbol == "L":
            interval_a = guess + 1
            guess = (guess + interval_b) // 2
        elif input_symbol == "H":
            interval_b = guess - 1
            guess = (interval_a + guess) // 2
        else:
            print("The correct secret number is {}.".format(guess))
            break


def reversed_guessing_game(min, max):
    interval_a = min
    interval_b = max + 1
    guess = (interval_a + interval_b) // 2
    print(
        "Please choose a secret number in the interval [1,100].Then enter one of L (if the guess was lower than the secret number), H (if the guess was higher than the secret number) or C (if the guess was correct).")
    while True:
        print("The secret number is {}. Is it right?".format(guess))
        print("Please enter one of L, H, or C: ", end="")
        input_symbol = input().lower()
        if input_symbol == "L":
            interval_a = guess + 1
            guess = (guess + interval_b) // 2
        elif input_symbol == "H":
            interval_b = guess - 1
            guess = (interval_a + guess) // 2
        else:
            print("The correct secret number is {}.".format(guess))
            break
