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
        print("Hi there! How's it going?")
    
    elif "how are you" in user_input:
        print("I'm doing great!")
    
    elif "your name" in user_input or "who are you" in user_input:
        print("I'm PyBot, your friendly Python assistant!")
    
    elif "weather" in user_input:
        print("I can't check real weather yet, but I can help you if you decide about a jacket.")
        weather_input = input("Is it cold, chilly, freezing, warm, hot, or sunny outside? ").lower().strip()
      
        if weather_input in ["cold", "chilly", "freezing"]:
            print("You should definitely wear a jacket!")
    
        elif weather_input in ["warm", "hot", "sunny"]:
            print("No jacket needed, enjoy the weather!")
        else:
            print("I'll assume it's mild weather. A light jacket might be a good idea!") # Added a default response for unrecognized weather input
    
    elif "joke" in user_input or "funny" in user_input:
        print("Why did the chicken cross the road? To get to the other side!")
    elif "help" in user_input:
        print("You can say hello, ask about the weather, ask for a joke, or type quit.")
    else:
        print("Hmm, I didn't understand that.")
    return True


def main() -> None:
    """Main function to run PyBot conversation loop."""
    print("Hello! I'm PyBot. Type 'quit' to exit.")
    
    while True:
        user_input = input("").lower().strip() # Makes the input easier to work with by converting to lowercase and removing extra spaces
        if not process_input(user_input):
            break


if __name__ == "__main__":
    main()