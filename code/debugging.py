"""
Debugging - Finding and Fixing Code Mysteries

Extracted from the companion book.
"""

import random
import logging
import datetime
import os

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='chatbot_debug.log'
)

# Response patterns
response_patterns = {
    "greetings": ["hello", "hi", "hey", "howdy", "hola"],
    "farewells": ["bye", "goodbye", "see you", "cya", "farewell"],
    "gratitude": ["thanks", "thank you", "appreciate"],
    "bot_questions": ["who are you", "what are you", "your name"],
    "user_questions": ["how are you", "what's up", "how do you feel"]
}

response_templates = {
    "greetings": ["Hello there!", "Hi! Nice to chat with you!"],
    "farewells": ["Goodbye! Come back soon!", "See you later!"],
    "gratitude": ["You're welcome!", "Happy to help!"],
    "bot_questions": ["I'm PyBot, a simple chatbot built with Python!"],
    "user_questions": ["I'm functioning well, thanks for asking!"]
}

class DebugChatbot:
    """A chatbot with enhanced debugging capabilities."""

    def __init__(self, name="PyBot"):
        self.name = name
        self.user_name = None
        self.conversation_history = []
        self.response_patterns = response_patterns
        self.response_templates = response_templates
        self.debug_mode = False
        logging.info(f"Chatbot {name} initialized")

    def toggle_debug(self):
        """Toggle debug mode on/off."""
        self.debug_mode = not self.debug_mode
        status = "ON" if self.debug_mode else "OFF"
        logging.info(f"Debug mode turned {status}")
        return f"Debug mode is now {status}"

    def debug_print(self, message):
        """Print debug messages if debug mode is on."""
        if self.debug_mode:
            print(f"DEBUG: {message}")
        logging.debug(message)

    def get_response(self, user_input):
        """Generate a response with debugging information."""
        self.debug_print(f"Processing input: '{user_input}'")

        if not user_input:
            self.debug_print("Empty input received")
            return "I didn't catch that. Could you please say something?"

        user_input = user_input.lower()
        self.debug_print(f"Lowercase input: '{user_input}'")

        # Check if this is a debug command
        if user_input == "debug":
            return self.toggle_debug()

        # Check each category of responses
        for category, patterns in self.response_patterns.items():
            self.debug_print(f"Checking category: {category}")

            for pattern in patterns:
                if pattern in user_input:
                    self.debug_print(f"Pattern match found: '{pattern}'")

                    # Get response templates for this category
                    templates = self.response_templates.get(category)
                    self.debug_print(f"Found {len(templates)} possible responses")

                    # Select a random response
                    response = random.choice(templates)
                    self.debug_print(f"Selected response: '{response}'")
                    return response

        # No pattern matched
        self.debug_print("No pattern matches found")
        return "I'm still learning. Can you tell me more?"

    def run(self):
        """Run the chatbot with error tracing."""
        try:
            print(f"Hello! I'm {self.name}. Type 'bye' to exit or 'debug' to toggle debug mode.")
            self.user_name = input("What's your name? ")
            logging.info(f"User identified as {self.user_name}")
            print(f"Nice to meet you, {self.user_name}!")

            self.add_to_history(self.name, f"Nice to meet you, {self.user_name}!")

            while True:
                try:
                    user_input = input(f"{self.user_name}> ")
                    self.add_to_history(self.user_name, user_input)

                    if user_input.lower() in ["bye", "goodbye", "exit"]:
                        response = f"Goodbye, {self.user_name}!"
                        print(f"{self.name}> {response}")
                        self.add_to_history(self.name, response)
                        break

                    response = self.get_response(user_input)
                    print(f"{self.name}> {response}")
                    self.add_to_history(self.name, response)

                except Exception as e:
                    error_msg = f"Error in conversation loop: {str(e)}"
                    logging.error(error_msg, exc_info=True)
                    if self.debug_mode:
                        print(f"DEBUG ERROR: {error_msg}")
                    print(f"{self.name}> Sorry, I encountered a problem. Let's continue.")

        except Exception as e:
            logging.critical(f"Critical error in chatbot: {str(e)}", exc_info=True)
            print(f"Critical error: {str(e)}")
            print("Check the log file for details.")

    def add_to_history(self, speaker, text):
        """Add a message to conversation history with timestamp."""
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        entry = {
            "speaker": speaker,
            "text": text,
            "timestamp": timestamp
        }
        self.conversation_history.append(entry)
        self.debug_print(f"Added to history: {entry}")

# Create and run the chatbot
if __name__ == "__main__":
    chatbot = DebugChatbot()
    chatbot.run()
