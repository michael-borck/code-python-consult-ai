"""
Values - Understanding Python's Data Types

Extracted from the companion book.
"""

"""
PyBot: A simple Python chatbot
Version 0.3: Adding different data types
"""

# Configuration constants
BOT_NAME = "PyBot"
VERSION = "0.3"
CREATOR = "Your Name"

# Bot characteristics using different data types
bot_properties = {
    "name": BOT_NAME,           # String
    "version": VERSION,         # String
    "creation_year": 2023,      # Integer
    "is_active": True,          # Boolean
    "response_time_ms": 10.5,   # Float
    "capabilities": [           # List
        "greeting",
        "basic conversation",
        "version info"
    ],
    "advanced_features": None   # None (for future development)
}

# Display the bot information
def display_bot_info():
    """Display information about the bot using different data types."""
    # Creating a border with string repetition
    border = "=" * 50

    print(border)
    print(f"{bot_properties['name']} v{bot_properties['version']} Information")
    print(border)

    # Looping through list items
    print("\nCapabilities:")
    for i, capability in enumerate(bot_properties['capabilities'], 1):
        print(f"  {i}. {capability}")

    # Using boolean for conditional message
    status = "active" if bot_properties['is_active'] else "inactive"
    print(f"\nCurrent Status: {status}")

    # Using numeric types for calculations
    uptime_days = 365 - (365 * 0.05)  # 95% uptime example
    print(f"Expected Annual Uptime: {uptime_days:.1f} days")

    # Using None check for conditional display
    if bot_properties['advanced_features'] is None:
        print("\nAdvanced features: Coming soon!")
    else:
        print(f"\nAdvanced features: {bot_properties['advanced_features']}")

    print(border)

# Display chatbot greeting with string formatting
def display_greeting():
    """Display the bot's greeting message."""
    name = bot_properties['name']
    version = bot_properties['version']

    # Using string concatenation and formatting
    greeting_message = (
        f"Hello! I'm {name} v{version}.\n"
        f"I'm a chatbot built with Python.\n"
        f"I can respond to basic commands and questions."
    )

    print(f"{name}> {greeting_message}")

# Run our enhanced chatbot
display_bot_info()
display_greeting()
