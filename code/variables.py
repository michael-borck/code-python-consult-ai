"""
Variables - Storing and Managing Data

Extracted from the companion book.
"""

"""
PyBot: A Python chatbot with memory
Version 0.4: Using variables to track state
"""

# Bot configuration (constants)
BOT_NAME = "PyBot"
VERSION = "0.4"
CREATOR = "Your Name"

# Bot state variables (will change during execution)
user_name = None
message_count = 0
last_topic = None
greeting_shown = False
favorite_color = None

# Display personalized greeting
def display_greeting():
    """Display greeting based on chatbot state."""
    global greeting_shown, user_name

    if not greeting_shown:
        # First-time greeting
        print(f"{BOT_NAME}> Hello! I'm {BOT_NAME}, version {VERSION}.")
        user_input = input("What's your name? ")
        user_name = user_input  # Store name in a variable for later use
        print(f"{BOT_NAME}> Nice to meet you, {user_name}!")
        greeting_shown = True  # Update state variable
    else:
        # Returning user greeting
        print(f"{BOT_NAME}> Welcome back, {user_name}!")

# Process user message
def process_message(message):
    """Process user message and update state variables."""
    global message_count, last_topic, favorite_color

    # Increment message counter
    message_count += 1

    # Convert to lowercase for easier processing
    message = message.lower()

    # Update last topic based on message content
    if "weather" in message:
        last_topic = "weather"
    elif "food" in message:
        last_topic = "food"
    elif "color" in message:
        last_topic = "color"

        # If user mentions their favourite color, store it
        if "favourite" in message and "is" in message:
            # Simple color extraction (will improve in later chapters)
            words = message.split()
            for i, word in enumerate(words):
                if word == "is" and i < len(words) - 1:
                    favorite_color = words[i + 1].lower()
                    break

    # Respond based on state variables
    if message_count == 1:
        return f"That's your first message! Thanks for chatting with me."
    elif "color" in message and favorite_color:
        return f"I remember your favourite color is {favorite_color}!"
    elif last_topic:
        return f"I see we're talking about {last_topic} now."
    else:
        return f"Thanks for your message. That's {message_count} messages so far!"

# Display chatbot status using state variables
def display_status():
    """Show current chatbot state using tracked variables."""
    print("\n" + "=" * 50)
    print(f"{BOT_NAME} Status:")
    print(f"User: {user_name if user_name else 'Unknown'}")
    print(f"Messages received: {message_count}")
    print(f"Last topic: {last_topic if last_topic else 'None'}")
    if favorite_color:
        print(f"User's favourite color: {favorite_color}")
    print("=" * 50 + "\n")

# Run a simple chat session
display_greeting()

# Simulate a conversation
while True:
    # Get user input
    user_message = input(f"{user_name}> ")

    # Check for exit command
    if user_message.lower() in ["exit", "quit", "bye"]:
        print(f"{BOT_NAME}> Goodbye, {user_name}! It was nice chatting with you.")
        break

    # Check for status command
    if user_message.lower() == "status":
        display_status()
        continue

    # Process message and respond
    response = process_message(user_message)
    print(f"{BOT_NAME}> {response}")
