# Importing required libraries
import random

# Dictionary of predefined responses
responses = {
    "greeting": ["Hello!", "Hi!", "Welcome!"],
    "farewell": ["Goodbye!", "See you later!", "Take care!"],
    "thanks": ["You're welcome!", "No problem!", "My pleasure!"],
    "default": ["I'm sorry, I didn't understand.", 
                "Could you please rephrase that?", 
                "I'm still learning. Can you provide more information?"]
}

# Function to generate a response based on user input
def generate_response(user_input):
    user_input = user_input.lower()

    # Check for common keywords in user input
    if "hello" in user_input or "hi" in user_input:
        return random.choice(responses["greeting"])
    elif "goodbye" in user_input or "bye" in user_input:
        return random.choice(responses["farewell"])
    elif "thank" in user_input:
        return random.choice(responses["thanks"])
    else:
        return random.choice(responses["default"])

print("Type 'exit' to end the chat.\n")

# Main interaction loop
while True:
    # Get user input
    user_input = input("User: ")

    # Exit condition
    if user_input.lower() in ["exit", "quit"]:
        print("Bot: Goodbye! Have a nice day!")
        break

    # Generate and display bot response
    bot_response = generate_response(user_input)
    print("Bot:", bot_response)