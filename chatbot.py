print("Hi! I am CodSoft Chatbot. Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "hi" or user == "hello":
        print("Bot: Hello! How can I help you?")
    elif "name" in user:
        print("Bot: I am CodSoft AI Bot.")
    elif "internship" in user:
        print("Bot: CodSoft internship helps students gain practical skills.")
    elif "bye" in user:
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: Sorry, I don't understand.")