import random


def guessing_game():
    n = random.randint(1, 100)
    counter = 1
    input_integer = int(input("Please enter an integer: "))
    while input_integer != n:
        counter += 1
        if input_integer < n:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
        input_integer = int(input("Please enter an integer again: "))
    print("Congratulations! You take {} guesses to reach the correct answer.".format(counter))


def reversed_guessing_game():
    interval_a = 1
    interval_b = 101
    guess = (interval_a + interval_b) // 2
    print(
        "Please choose a secret number in the interval [1,100].Then enter one of L (if the guess was lower than the "
        "secret number), H (if the guess was higher than the secret number) or C (if the guess was correct).")
    while True:
        print("The secret number is {}. Is it right?".format(guess))
        input_symbol = input("Please enter one of L, H, or C: ")
        if input_symbol == "L":
            interval_a = guess + 1
            guess = (guess + interval_b) // 2
        elif input_symbol == "H":
            interval_b = guess
            guess = (interval_a + guess) // 2
        elif input_symbol == "C":
            print("The correct secret number is {}.".format(guess))
            break


def revised_reversed_guessing_game(min, max):
    interval_a = min
    interval_b = max + 1
    guess = (interval_a + interval_b) // 2
    print(
        "Please choose a secret number in the interval [1,100].Then enter one of L (if the guess was lower than the "
        "secret number), H (if the guess was higher than the secret number) or C (if the guess was correct).")
    while True:
        print("The secret number is {}. Is it right?".format(guess))
        input_symbol = input("Please enter one of L, H, or C: ").lower()
        if input_symbol == "l":
            if interval_a == guess:
                print("You are cheating!")
            else:
                interval_a = guess + 1
                guess = (guess + interval_b) // 2
        elif input_symbol == "h":
            if interval_b == guess:
                print("You are cheating!")
            else:
                interval_b = guess
                guess = (interval_a + guess) // 2
        elif input_symbol == "c":
            print("The correct secret number is {}.".format(guess))
            break
        else:
            print("You are cheating!")


reversed_guessing_game()
# revised_reversed_guessing_game(1, 10000)
