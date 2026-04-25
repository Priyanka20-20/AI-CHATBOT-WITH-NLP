while True:
    user_input = input("You: ").lower()

    if user_input == "bye":
        print("Chatbot: Goodbye!")
        break

    words = user_input.split()

    if "hello" in words or "hi" in words:
        print("Chatbot: Hello! How can I help you?")
    
    elif "name" in words:
        print("Chatbot: I am a simple chatbot.")
    
    elif "age" in words:
        print("Chatbot: I don't have an age.")
    
    elif "help" in words:
        print("Chatbot: Ask me about name, age, weather, etc.")
    
    elif "weather" in words:
        print("Chatbot: I cannot check live weather.")
    
    else:
        print("Chatbot: Sorry, I didn’t understand.")
