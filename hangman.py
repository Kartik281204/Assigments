import random
words = ("apple", "banana", "spinach", "tomato", "carrot")
hangman_art = {
    0: ("   ",
        "   ",
        "   "),
    1:  (" O  ",
         "   ",
         "   "),
    2:  (" O  ",
         "/   ",
         "   "),
    3:  (" O  ",
         "/ \\",
         "   "),
    4:  (" O  ",
         "/|\\",
         "   "),
    5:  (" O  ",
         "/|\\",
         "/   "),
    6:  (" O  ",
         "/|\\  ",
         "/ \\  ")}


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
    hints = ["_"]*len(answer)
    print("----------------------")
    display_hint(hints)
    print("----------------------")
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hints)
        guess = input("Enter your guess : ").lower()
        if guess == "Exit".lower():
            break
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input try again")
            continue
        if guess in guessed_letters:
            print("Letter already guessed")
            continue
        guessed_letters.add(guess)
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hints[i] = guess

        else:
            wrong_guesses += 1
        if "_" not in hints:
            display_answer(answer)
            display_man(wrong_guesses)
            print("You win")
            is_running = False
        elif wrong_guesses >= len(hangman_art):
            display_answer(answer)
            display_man(wrong_guesses)
            print("You lose!!!!!")
            is_running = False


if __name__ == "__main__":
    main()
