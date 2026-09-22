import random

words = ("apple", "banana", "spinach", "tomato", "carrot")

hangman_art = {
    0: ("   ",
        "   ",
        "   "),
    1: (" O  ",
        "   ",
        "   "),
    2: (" O  ",
        "/   ",
        "   "),
    3: (" O  ",
        "/ \\",
        "   "),
    4: (" O  ",
        "/|\\",
        "   "),
    5: (" O  ",
        "/|\\",
        "/   "),
    6: (" O  ",
        "/|\\",
        "/ \\")
}


def display_man(wrong_guesses):
    print("----------------------")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("----------------------")


def display_answer(answer):
    print(" ".join(answer))


def display_hint(hints):
    print(" ".join(hints))


def main():
    answer = random.choice(words)
    hints = ["_"] * len(answer)      # Fixed: make hints a list

    print("----------------------")
    display_hint(hints)
    print("----------------------")

    wrong_guesses = 0                # Start with an empty hangman
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hints)

        guess = input("Enter your guess: ").lower()

        if guess == "exit":
            break

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hints[i] = guess

        # You can continue from here by handling wrong guesses,
        # checking for win/loss, etc.


if __name__ == "__main__":
    main()
