
import random

# Define a dictionary of possible user inputs and corresponding bot responses
conversations ={
    "hello": ["Hello!", "Hi there!", "Hey!"],
    "how are you?": ["I'm good, thanks!", "Feeling great!", "I'm doing well."],
    "bye": ["Goodbye!", "Bye bye!", "See you later!"],
    "default": ["That's interesting!", "Tell me more...", "I'm not sure I understand."],
}

def get_bot_response(user_input):
    user_input = user_input.lower()  # Convert user input to lowercase
    if user_input in conversations:
        return random.choice(conversations[user_input])
    else:
        return random.choice(conversations["default"])

def main():
    print("Welcome to the ChatBot!")
    print("You can start chatting with me. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'bye':
            print(get_bot_response(user_input))
            break
        
        response = get_bot_response(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    main()
