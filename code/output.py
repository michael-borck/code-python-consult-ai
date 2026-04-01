"""
Output - Communicating with the World

Extracted from the companion book.
"""

import time

def simulate_chatbot_conversation():
    """Simulate a conversation with our chatbot using different output techniques."""
    bot_name = "PyBot"
    width = 60

    # Welcome screen
    print("\n" + "=" * width)
    print(f"{bot_name} Chat Simulation".center(width))
    print("=" * width)

    # Initial greeting
    print(f"\n{bot_name}> Hello! I'm {bot_name}, your Python assistant.")
    time.sleep(1)
    print(f"{bot_name}> What's your name?")

    # Simulate user input
    time.sleep(1.5)
    user_name = "Alex"
    print(f"{user_name}> My name is {user_name}.")

    # Bot response with formatted output
    time.sleep(1)
    print(f"{bot_name}> Nice to meet you, {user_name}!")
    time.sleep(0.8)
    print(f"{bot_name}> I can help you learn Python concepts.")

    # System message
    time.sleep(1.2)
    print(f"[SYSTEM] {bot_name} is retrieving information...")
    time.sleep(1.5)

    # Information display with structure
    print(f"\n{bot_name}> Here are today's Python topics:")
    print("  • Variables and data types")
    print("  • Input and output techniques")
    print("  • String formatting with f-strings")
    print("  • Basic control structures")

    # Error message simulation
    time.sleep(1.5)
    print(f"\n{user_name}> Can you write my homework for me?")
    time.sleep(1.2)
    print(f"{bot_name} [ERROR]> I'm designed to help you learn, not to do your work for you.")
    print("*" * 65)

    # Help message
    time.sleep(1.5)
    print(f"\n{user_name}> help")
    time.sleep(1)
    print("\n" + "-" * width)
    print(f"{bot_name} HELP".center(width))
    print("-" * width)
    print("""
Commands you can try:
- ASK [question]: Ask me about Python
- TOPICS: Show available topics
- EXAMPLE [topic]: Get an example about a topic
- BYE: End our conversation
    """)
    print("-" * width)

    # Ending the conversation
    time.sleep(1.5)
    print(f"\n{user_name}> bye")
    time.sleep(1)
    print(f"{bot_name}> Goodbye, {user_name}! Happy coding!")
    print("\n" + "=" * width)
    print("End of simulation".center(width))
    print("=" * width + "\n")

# Run the simulation
simulate_chatbot_conversation()
