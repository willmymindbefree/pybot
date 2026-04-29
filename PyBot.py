import hangman
import tictactoe


def handle_greeting() -> None:
    print("Hi there! How's it going?")


def handle_how_are_you() -> None:
    print("I'm doing great!")


def handle_name_query() -> None:
    print("I'm PyBot, your friendly Python assistant!")


def handle_weather() -> None:
    """
        Handle weather-related queries and clothing suggestions.
    """
    print("I can't check real weather yet, but I can help you if you decide about a jacket.")
    weather_input = input("Is it cold, chilly, freezing, warm, hot, or sunny outside? ").lower().strip()
    
    if weather_input in ["cold", "chilly", "freezing"]:
        print("You should definitely wear a jacket!")
    elif weather_input in ["warm", "hot", "sunny"]:
        print("No jacket needed, enjoy the weather!")
    else:
        print("I'll assume it's mild weather. A light jacket might be a good idea!")


def handle_joke() -> None:
    """
        Tell a joke to the user.
    """
    print("Why did the chicken cross the road? To get to the other side!")


def handle_help() -> None:
    """
        Display help information about available commands.
    """
    print("You can say hello, ask about the weather, ask for a joke, or type quit.")


def handle_unknown() -> None:
    """
        Handle unrecognized user input.
    """
    print("Hmm, I didn't understand that.")


def handle_hangman() -> None:
    """
        Offer to play hangman game.
    """
    hangman.play_hangman()

def handle_tictactoe() -> None:
    """
        Offer to play Tic-Tac-Toe!
    """
    tictactoe.play()


def process_input(user_input: str) -> bool:
    """
        Processes user input and Returns False if the user wants to quit
        Arguments - user_input: The input string from the user
        Return value - bool:
    
    """
    if user_input == "quit":
        print("Goodbye! Have a nice day")
        return False
    
    elif "hello" in user_input or "hi" in user_input or "hey" in user_input:
        handle_greeting()
    
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
    """
        Main function to run PyBot.
    """
    print("Hello! I'm PyBot. Type 'quit' to exit.")
    
    while True:
        user_input = input("").lower().strip() # Makes the input easier to work with by converting to lowercase and removing extra spaces
        if not process_input(user_input):
            break


if __name__ == "__main__":
    main()