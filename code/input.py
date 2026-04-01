"""
Input - The Gateway to User Interaction

Extracted from the companion book.
"""

def enhanced_chatbot():
    """An enhanced chatbot with input validation and better responses."""
    bot_name = "PyBot"

    # Welcome message with formatting
    print("\n" + "=" * 60)
    print(f"{bot_name} - Your Python Learning Assistant".center(60))
    print("=" * 60 + "\n")

    print(f"{bot_name}> Hello! I'm {bot_name}. What's your name?")

    # Get user's name with validation
    while True:
        user_name = input("You> ").strip()
        if user_name:  # Check that name isn't empty
            break
        print(f"\n{bot_name}> I didn't catch that. Could you tell me your name again?")

    print(f"\n{bot_name}> Nice to meet you, {user_name}!")
    print(f"{bot_name}> I can help with Python questions or just chat.")
    print(f"{bot_name}> Type 'help' for options or 'bye' to exit.")

    # Track conversation state
    question_count = 0

    # Main conversation loop
    while True:
        # Get user input
        user_input = input(f"\n{user_name}> ").strip()

        # Skip empty inputs
        if not user_input:
            print(f"\n{bot_name}> Did you want to ask something?")
            continue

        # Convert to lowercase for processing
        user_input_lower = user_input.lower()

        # Check for exit command
        if user_input_lower in ["bye", "goodbye", "exit", "quit"]:
            print(f"\n{bot_name}> Goodbye, {user_name}! I enjoyed our conversation.")
            break

        # Process input and generate responses
        if user_input_lower in ["hello", "hi", "hey", "greetings"]:
            print(f"\n{bot_name}> Hello again, {user_name}! How can I help you today?")

        elif "how are you" in user_input_lower:
            print(f"\n{bot_name}> I'm functioning perfectly! Thanks for asking.")
            print(f"{bot_name}> How are you doing today?")

        elif user_input_lower == "help":
            print(f"\n{bot_name}> Here's what you can ask me about:")
            print(f"{bot_name}> - Say hello or ask how I'm doing")
            print(f"{bot_name}> - Ask about Python concepts")
            print(f"{bot_name}> - Ask about my capabilities")
            print(f"{bot_name}> - Type 'bye' to end our conversation")

        elif "your name" in user_input_lower:
            print(f"\n{bot_name}> My name is {bot_name}. I'm a Python-powered chatbot!")

        elif "python" in user_input_lower:
            print(f"\n{bot_name}> Python is a versatile programming language!")
            print(f"{bot_name}> Is there something specific about Python you'd like to know?")

        elif any(word in user_input_lower for word in ["thanks", "thank you"]):
            print(f"\n{bot_name}> You're welcome, {user_name}! Happy to help.")

        elif "?" in user_input:
            question_count += 1
            print(f"\n{bot_name}> That's a good question! As we progress through this book,")
            print(f"{bot_name}> I'll learn to answer more complex questions like that.")
            print(f"{bot_name}> You've asked {question_count} question(s) so far.")

        else:
            print(f"\n{bot_name}> That's interesting! As a simple chatbot, I'm still")
            print(f"{bot_name}> learning how to respond to a wide range of topics.")
            print(f"{bot_name}> Try asking me something about Python or type 'help'.")

    # Farewell message
    print("\n" + "-" * 60)
    print("Chat session ended. Thanks for talking with PyBot!".center(60))
    print("-" * 60 + "\n")

# Run the enhanced chatbot (commented out to avoid execution)
# enhanced_chatbot()
