"""
Files - Persisting Your Data

Extracted from the companion book.
"""

import datetime
import os
import random

# Using dictionaries for response patterns
response_patterns = {
    "greetings": ["hello", "hi", "hey", "howdy", "hola"],
    "farewells": ["bye", "goodbye", "see you", "cya", "farewell"],
    "gratitude": ["thanks", "thank you", "appreciate"],
    "bot_questions": ["who are you", "what are you", "your name"],
    "user_questions": ["how are you", "what's up", "how do you feel"]
}

response_templates = {
    "greetings": ["Hello there! How can I help you today?", "Hi! Nice to chat with you!"],
    "farewells": ["Goodbye! Come back soon!", "See you later! Have a great day!"],
    "gratitude": ["You're welcome!", "Happy to help!"],
    "bot_questions": ["I'm PyBot, a simple chatbot built with Python!"],
    "user_questions": ["I'm functioning well, thanks for asking!"]
}

def get_response(user_input):
    """Get a response based on the user input."""
    user_input = user_input.lower()

    # Check each category of responses
    for category, patterns in response_patterns.items():
        for pattern in patterns:
            if pattern in user_input:
                # Return a random response from the appropriate category
                return random.choice(response_templates[category])

    # Default response if no patterns match
    return "I'm still learning. Can you tell me more?"

def save_conversation():
    """Save the current conversation to a file."""
    # Create 'chats' directory if it doesn't exist
    if not os.path.exists('chats'):
        os.makedirs('chats')

    # Generate a unique filename with timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"chats/chat_with_{user_name}_{timestamp}.txt"

    try:
        with open(filename, "w") as f:
            # Write header information
            f.write(f"Conversation with {bot_name} and {user_name}\n")
            f.write(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

            # Write each line of conversation
            for entry in conversation_history:
                f.write(f"{entry}\n")

        return filename
    except Exception as e:
        return f"Error saving conversation: {str(e)}"

def load_conversation(filename):
    """Load a previous conversation from a file."""
    try:
        with open(filename, "r") as f:
            lines = f.readlines()

        print("\n----- Loaded Conversation -----")
        for line in lines:
            print(line.strip())
        print("-------------------------------\n")
        return True
    except FileNotFoundError:
        print(f"Sorry, I couldn't find the file '{filename}'.")
        # Show available files
        show_available_chats()
        return False
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False

def show_available_chats():
    """Show a list of available saved conversations."""
    if not os.path.exists('chats'):
        print("No saved conversations found.")
        return

    chat_files = os.listdir('chats')
    if not chat_files:
        print("No saved conversations found.")
        return

    print("\nAvailable saved conversations:")
    for i, chat_file in enumerate(chat_files, 1):
        print(f"{i}. {chat_file}")
    print("\nTo load a conversation, type 'load' followed by the filename.")

# Main chat loop
bot_name = "PyBot"
print(f"Hello! I'm {bot_name}. Type 'bye' to exit.")
print("Special commands:")
print("- 'save': Save the current conversation")
print("- 'chats': Show available saved conversations")
print("- 'load <filename>': Load a conversation")

user_name = input("What's your name? ")
print(f"Nice to meet you, {user_name}!")

conversation_history = []

def save_to_history(speaker, text):
    """Save an utterance to conversation history."""
    conversation_history.append(f"{speaker}: {text}")

# Save initial greeting
save_to_history(bot_name, f"Nice to meet you, {user_name}!")

while True:
    user_input = input(f"{user_name}> ")
    save_to_history(user_name, user_input)

    # Check for special commands
    if user_input.lower() == "bye":
        response = f"Goodbye, {user_name}!"
        print(f"{bot_name}> {response}")
        save_to_history(bot_name, response)
        break
    elif user_input.lower() == "save":
        filename = save_conversation()
        print(f"{bot_name}> Conversation saved to {filename}")
        save_to_history(bot_name, f"Conversation saved to {filename}")
        continue
    elif user_input.lower() == "chats":
        show_available_chats()
        continue
    elif user_input.lower().startswith("load "):
        filename = user_input[5:].strip()
        load_conversation(filename)
        continue

    # Get and display response
    response = get_response(user_input)
    print(f"{bot_name}> {response}")
    save_to_history(bot_name, response)
