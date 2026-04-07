print("Hello! I'm Pybot. Type quit to exit.")

while True:
    user_input = input("You: ").lower().strip()  # Make it lowercase and clean
    
    if user_input == "quit":
        print("Goodbye! Have a nice day")
        break
    
    elif "hello" in user_input or "hi" in user_input or "hey" in user_input:
        print("Hi there! How's it going?")
    
    elif "how are you" in user_input:
        print("I'm doing great!")
    
    elif "your name" in user_input:
        print("I'm Pybot, your friendly Python assistant!")
    
    elif "weather" in user_input:
        print("I can't check real weather yet, but I can tell you if you should wear a jacket!\n What's the temperature like outside?")
    
    elif cold := ["cold", "chilly", "freezing"]:
        print("You should definitely wear a jacket!")
    
    elif warm := ["warm", "hot", "sunny"]:
        print("No jacket needed, enjoy the weather!")
    
    elif "joke" in user_input or "funny" in user_input:
        print("Why did the chicken cross the road? To get to the other side!")
    
    else:
        print("Hmm, I didn't understand that.")