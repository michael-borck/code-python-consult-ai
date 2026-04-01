"""
Errors and Exceptions - Handling the Unexpected

Extracted from the companion book.
"""

import os
import datetime
import random

# Response patterns and templates from Chapter 14
response_patterns = {
    "greetings": ["hello", "hi", "hey", "howdy"],
    "farewells": ["bye", "goodbye", "see you", "cya"],
    # other patterns...
}

response_templates = {
    "greetings": ["Hello there!", "Hi! Nice to chat with you!"],
    "farewells": ["Goodbye! Come back soon!", "See you later!"],
    # other templates...
}

def get_response(user_input):
    """Get a response based on the user input."""
    user_input = user_input.lower()

    for category, patterns in response_patterns.items():
        for pattern in patterns:
            if pattern in user_input:
                return random.choice(response_templates[category])

    return "I'm still learning. Can you tell me more?"

def save_conversation():
    """Save the current conversation to a file with error handling."""
    try:
        # Create the chats directory if it doesn't exist
        if not os.path.exists('chats'):
            os.makedirs('chats')

        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"chats/chat_with_{user_name}_{timestamp}.txt"

        with open(filename, "w") as f:
            f.write(f"Conversation with {bot_name} and {user_name}\n")
            f.write(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

            for entry in conversation_history:
                f.write(f"{entry}\n")

        return f"Conversation saved to {filename}"
    except PermissionError:
        return "Sorry, I don't have permission to save in that location."
    except OSError as e:
        return f"Error saving conversation: {str(e)}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

def load_conversation(filename):
    """Load a previous conversation from a file with error handling."""
    try:
        # Make sure the file is in the chats directory for security
        if not filename.startswith('chats/'):
            filename = f"chats/{filename}"

        with open(filename, "r") as f:
            lines = f.readlines()

        print("\n----- Loaded Conversation -----")
        for line in lines:
            print(line.strip())
        print("-------------------------------\n")
        return True
    except FileNotFoundError:
        print(f"{bot_name}> Sorry, I couldn't find the file '{filename}'.")
        show_available_chats()
        return False
    except PermissionError:
        print(f"{bot_name}> I don't have permission to read that file.")
        return False
    except UnicodeDecodeError:
        print(f"{bot_name}> That doesn't appear to be a text file I can read.")
        return False
    except Exception as e:
        print(f"{bot_name}> An error occurred: {str(e)}")
        return False

def show_available_chats():
    """Show a list of available saved conversations with error handling."""
    try:
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
    except Exception as e:
        print(f"Error listing conversations: {str(e)}")

def get_valid_input(prompt, validation_func=None, error_message=None):
    """Repeatedly prompt the user until valid input is received."""
    while True:
        user_input = input(prompt)

        # If no validation function was provided, any input is valid
        if validation_func is None:
            return user_input

        # Check if the input is valid
        if validation_func(user_input):
            return user_input

        # Display error message and try again
        if error_message:
            print(error_message)

# Main chat loop
bot_name = "PyBot"
print(f"Hello! I'm {bot_name}. Type 'bye' to exit.")
print("Special commands:")
print("- 'save': Save the current conversation")
print("- 'chats': Show available saved conversations")
print("- 'load <filename>': Load a conversation")

# Get user name with validation
def is_valid_name(name):
    return len(name.strip()) > 0

user_name = get_valid_input(
    "What's your name? ",
    is_valid_name,
    "Name cannot be empty. Please enter your name."
)
print(f"Nice to meet you, {user_name}!")

conversation_history = []

def save_to_history(speaker, text):
    """Save an utterance to conversation history."""
    conversation_history.append(f"{speaker}: {text}")

# Save initial greeting
save_to_history(bot_name, f"Nice to meet you, {user_name}!")

while True:
    try:
        user_input = input(f"{user_name}> ")
        save_to_history(user_name, user_input)

        # Check for special commands
        if user_input.lower() == "bye":
            response = f"Goodbye, {user_name}!"
            print(f"{bot_name}> {response}")
            save_to_history(bot_name, response)
            break

        elif user_input.lower() == "save":
            result = save_conversation()
            print(f"{bot_name}> {result}")
            save_to_history(bot_name, result)
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

    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        print(f"\n{bot_name}> Conversation interrupted. Goodbye!")
        break

    except Exception as e:
        # Catch-all for unexpected errors to prevent program crashes
        error_msg = f"I encountered an error: {str(e)}"
        print(f"{bot_name}> {error_msg}")
        save_to_history(bot_name, error_msg)
