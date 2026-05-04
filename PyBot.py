"""
    Group 5 - Pybot.py
    
    A bot that is great for trying out modular features in python.
    To-Do - add Finger Frenzy.
""" 
import json
import hangman
import tictactoe
import random

SAVE_FILE = 'pybotdata.json'
usage_data: dict[str, int] = {'tictactoe': 0, 'hangman': 0,}

def save():
    global usage_data
    try:
        with open(SAVE_FILE, 'w') as f:
            json.dump(usage_data, f)
    except Exception as e:
        print(f'{e}')
    

def load():
    """Saves current data (only two things)."""
    global usage_data
    try:
        with open(SAVE_FILE, 'r') as f:
            usage_data = json.load(f)
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f'error {e}')


def handle_greeting() -> None:
    print("Hi there! How's it going?")


def handle_how_are_you() -> None:
    print("I'm doing great!")


def handle_name_query() -> None:
    print("I'm PyBot, your Python assistant!")


def handle_weather() -> None:
    """Handle weather-related queries and clothing suggestions."""

    print("I can't check real weather yet, but I can help you if you decide about a jacket.")
    weather_input = input("Is it cold, chilly, freezing, warm, hot, or sunny outside? ").lower().strip()
    
    if weather_input in ["cold", "chilly", "freezing"]:
        print("You should definitely wear a jacket!")
    elif weather_input in ["warm", "hot", "sunny"]:
        print("No jacket needed, enjoy the weather!")
    elif weather_input in ["rainy", "snowy"]:
        print("You should bring an umbrella or wear something warm!")
    else:
        print("I'll assume it's mild weather. A light jacket might be a good idea!")


def handle_joke() -> None:
    """Tell a joke to the user."""
    print("Why did the chicken cross the road? To get to the other side!")


def handle_help() -> None:
    """Display help information about available commands."""

    print("Here are the commands you can use:")
    print("Hello")
    print("Weather")
    print("Joke")
    print("Hangman")
    print("TicTacToe - 2 Player")
    print("Quote")
    print("Help")
    print("Quit")


def handle_quote() -> None:
    """Give the user a motivational quote."""

    quotes = [
        "Keep going, you are doing better than you think.",
        "Every small step counts.",
        "Practice makes progress,",
        "Stay focused and keep learning."
    ]
    print(random.choice(quotes))


def handle_unknown() -> None:
    """Handle unrecognized user input."""

    print("Hmm, I didn't understand that.")


def handle_hangman() -> None:
    """Offer to play a hangman game."""
    usage_data['hangman'] += 1
    save()
    hangman.play_hangman()


def handle_tictactoe() -> None:
    """Offer to play a Tic-Tac-Toe game."""
    usage_data['tictactoe'] += 1
    save()
    tictactoe.main()
    match input('Want a rematch? (yes/no) '):
        case 'yes' | 'Yes' | 'y' | 'Yeah':
            handle_tictactoe()
        case '_':
            handle_greeting()
    

def process_input(user_input: str) -> bool:
    """
        Processes user input and Returns False if the user wants to quit
        Arguments - user_input: The input string from the user
        Return value - bool
    """
    # Bugs here from not checking for equal (==) is a known bug!
    if "quit" in user_input or "exit" in user_input:
        print("Goodbye! Have a nice day")
        return False
    
    elif "hello" in user_input or "hi" in user_input or "hey" in user_input:
        handle_greeting()

    elif "quote" in user_input or "motivation" in user_input:
        handle_quote()
    
    elif "how are you" in user_input:
        handle_how_are_you()
    
    elif "your name" in user_input or "who are you" in user_input:
        handle_name_query()
    
    elif "weather" in user_input:
        handle_weather()
    
    elif "joke" in user_input or "funny" in user_input:
        handle_joke()
    
    elif "help" in user_input:
        handle_help()
    
    elif "tic tac toe" in user_input or "tic-tac-toe" in user_input or "tictactoe" in user_input:
        handle_tictactoe()
    
    elif "hangman" in user_input:
        handle_hangman()

    else:
        handle_unknown()
    return True


def main() -> None:
    """Main loop to run PyBot."""
    load()
    print("Hello! I'm PyBot, your personalized assistant.")
    print("Type 'help' to see what I can do, or type 'quit' to exit.")
    
    try:
        while True:
            total_gaming: int = sum(usage_data.values())
            print(f"You have played Tic-tac-toe along with Hangman {total_gaming} times!")

            user_input = input("").lower().strip() # Makes the input easier to work with by converting to lowercase and removing extra spaces

            if not process_input(user_input):
                break
    except KeyboardInterrupt:
        save()


if __name__ == "__main__":
    main()
