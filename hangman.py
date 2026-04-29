# Hangman in Python
import random

hangman_art = {0: ("     ", "     ", "     "),
               1: ("   o ", "     ", "     "),
               2: ("   o ", "   | ", "     "),
               3: ("   o ", "  /| ", "     "),
               4: ("   o ", "  /|\\", "     "),
               5: ("   o ", "  /|\\", "  /  "),
               6: ("   o ", "  /|\\", "  / \\")}

def difficulty():       # Words can be changed without changing the code with text files 
    match input("Pick a difficulty or : command:\neasy\nregular\nhard\ninput :e :r :h to see the words: ").lower():
        case "easy":
            with open("easy_words.txt", "r") as file:
                lines1 = file.readlines()
                answer = random.choice(lines1).strip()
                return answer
        case "regular":
            with open("regular_words.txt", "r") as file:
                lines2 = file.readlines()
                answer = random.choice(lines2).strip()
                return answer
        case "hard":
            with open("hard_words.txt", "r") as file:
                lines3 = file.readlines()
                answer = random.choice(lines3).strip()
                return answer
        case ":e":
            with open("easy_words.txt", "r") as file:
                lines1 = file.readlines()
                print("Easy words:")
                for word in lines1:
                    print(word.strip())
                return difficulty()

        case ":r":
            with open("regular_words.txt", "r") as file:
                lines2 = file.readlines()
                print("Regular words:")
                for word in lines2:
                    print(word.strip())
                return difficulty()

        case ":h":
            with open("hard_words.txt", "r") as file:
                lines3 = file.readlines()
                print("Hard words:")
                for word in lines3:
                    print(word.strip())
                return difficulty()
        case ":q":
            print("Goodbye! Have a nice day")
            exit()
        
        case _:
            print("Invalid input")
            return difficulty()


def play_hangman() -> None:
    """Main hangman game function."""
    answer: str = difficulty()

    hint: list = ['_'] * len(answer)
    bad_guess: int = 0
    guessed = set()

    print("Welcome to Hangman!")
    print("Guess the word one letter at a time.")
    print(f"You have {len(hangman_art) - 1} incorrect guesses available.\n")

    while True:
        print("--------")
        for line in hangman_art[bad_guess]:
            print(line)
        print("--------")
        print("Word:", " ".join(hint))
        print("Guessed letters:", " ".join(sorted(guessed)))
        print("Remaining incorrect guesses:", (len(hangman_art) - 1) - bad_guess)

        guess: str = input("Enter a letter: ").lower() 

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue

        if guess in guessed:
            print(f"{guess} is already guessed")
            continue

        guessed.add(guess)

        if guess in answer: 
            print("Correct guess!")
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            print("Incorrect guess!")
            bad_guess += 1 
        
        if "_" not in hint:
            print("--------")
            for line in hangman_art[bad_guess]:
                print(line)
            print("--------")
            print(" ".join(answer))
            print("YOU WIN!")
            input("Press Enter to continue")
            break

        elif bad_guess >= len(hangman_art) - 1:
            print("--------")
            for line in hangman_art[bad_guess]:
                print(line)
            print("--------")
            print(" ".join(answer))
            print("YOU LOSE!")
            input("Press Enter to continue")
            break


if __name__ == "__main__":
    play_hangman()