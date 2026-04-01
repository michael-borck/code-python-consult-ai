"""
Python Language Syntax - Decoding the Code Language

Extracted from the companion book.
"""

#!/usr/bin/env python3
"""
PyBot: A simple Python chatbot
This file contains the core functionality for our chatbot project.
"""

# Configuration constants
BOT_NAME = "PyBot"
VERSION = "0.2"
CREATOR = "Your Name"

# Initialization function
def initialize_bot():
    """Set up the chatbot with initial configuration."""
    # Print welcome message
    print(f"{BOT_NAME} v{VERSION} initializing...")
    print("=" * 50)

    # Display bot introduction
    print(f"""
Welcome to {BOT_NAME}!
This is a simple chatbot that will grow more sophisticated
as we learn more Python concepts throughout this book.

Created by: {CREATOR}
    """)
    print("=" * 50)

# Main bot greeting function
def display_greeting():
    """Display the bot's greeting message to the user."""
    # Multi-line message with proper indentation
    greeting_message = (
        f"Hello! I'm {BOT_NAME}, your friendly Python assistant.\n"
        f"I'm currently pretty basic, but I'll learn new tricks\n"
        f"as you progress through the Python Jumpstart book!"
    )

    # Using the BOT_NAME constant for consistent naming
    print(f"{BOT_NAME}> {greeting_message}")

# Execute our chatbot code
initialize_bot()
display_greeting()
