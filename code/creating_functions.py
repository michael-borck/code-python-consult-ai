"""
Creating Functions - Build Your Own Python Tools

Extracted from the companion book.
"""

def get_user_name():
    """
    Get the user's name with basic validation.

    Returns:
        str: The user's name
    """
    while True:
        name = input("What's your name? ").strip()
        if name:  # Check that name isn't empty
            return name
        print("I didn't catch that. Please tell me your name.")

def display_welcome(bot_name):
    """
    Display the welcome message.

    Args:
        bot_name (str): The chatbot's name
    """
    print("\n" + "=" * 50)
    print(f"Welcome to {bot_name}!")
    print("=" * 50)
    print(f"Hello! I'm {bot_name}, a simple chatbot.")
    print("I can help you learn about Python functions.")
    print("Type 'bye' to exit, 'help' for commands.\n")

def get_user_input(user_name):
    """
    Get input from the user with their name as prompt.

    Args:
        user_name (str): The user's name

    Returns:
        str: The user's input
    """
    return input(f"{user_name}> ").strip()

def display_response(bot_name, response):
    """
    Display the chatbot's response.

    Args:
        bot_name (str): The chatbot's name
        response (str): The response to display
    """
    print(f"{bot_name}> {response}")

def get_response(user_input, user_name):
    """
    Generate a response based on user input.

    Args:
        user_input (str): The user's message
        user_name (str): The user's name

    Returns:
        str: The chatbot's response
    """
    user_input = user_input.lower()

    # Check for specific commands
    if user_input == "help":
        return get_help_message()

    # Check for greetings
    if any(greeting in user_input for greeting in ["hello", "hi", "hey"]):
        return f"Hello there, {user_name}!"

    # Check for questions about the bot
    if "your name" in user_input:
        return "My name is PyBot. I'm a simple chatbot built with Python functions!"

    if "how are you" in user_input:
        return "I'm just a computer program, but I'm functioning well. Thanks for asking!"

    # Check for farewells
    if any(farewell in user_input for farewell in ["bye", "goodbye", "exit"]):
        return f"Goodbye, {user_name}! Have a great day!"

    # Default response
    return "I'm not sure how to respond to that yet. Type 'help' for commands."

def get_help_message():
    """
    Return the help message.

    Returns:
        str: The help message
    """
    return """
I understand the following:
- Greetings (hello, hi)
- Questions about me
- 'how are you'
- 'bye' or 'goodbye' to exit
"""

def run_chatbot():
    """Run the main chatbot interaction loop."""
    bot_name = "PyBot"

    display_welcome(bot_name)
    user_name = get_user_name()
    print(f"\n{bot_name}> Nice to meet you, {user_name}!\n")

    while True:
        user_input = get_user_input(user_name)

        # Check for exit command
        if user_input.lower() == "bye":
            display_response(bot_name, f"Goodbye, {user_name}!")
            break

        response = get_response(user_input, user_name)
        display_response(bot_name, response)

# Run the chatbot if this file is executed directly
if __name__ == "__main__":
    run_chatbot()
