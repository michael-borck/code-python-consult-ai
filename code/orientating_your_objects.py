"""
Object-Oriented Programming in Python

Extracted from the companion book.
"""

class Chatbot:
    """A simple chatbot that becomes smarter as you learn Python."""

    def __init__(self, name="PyBot"):
        """Initialize the chatbot with a name and empty conversation history."""
        self.name = name
        self.user_name = None
        self.conversation_history = []
        self.response_patterns = {
            "greetings": ["hello", "hi", "hey", "howdy", "hola"],
            "farewells": ["bye", "goodbye", "see you", "cya", "farewell"],
            "gratitude": ["thanks", "thank you", "appreciate"],
            "bot_questions": ["who are you", "what are you", "your name"],
            "user_questions": ["how are you", "what's up", "how do you feel"]
        }

        self.response_templates = {
            "greetings": ["Hello, {user}!", "Hi there, {user}!", "Great to see you again!"],
            "farewells": ["Goodbye!", "See you later!", "Until next time!"],
            "gratitude": ["You're welcome!", "Happy to help!", "No problem at all."],
            "bot_questions": [f"I'm {name}, your chatbot assistant!", "I'm just a simple Python chatbot."],
            "user_questions": ["I'm just a program, but I'm working well!", "I'm here and ready to chat!"],
            "default": ["I'm not sure how to respond to that yet.", "Can you tell me more?", "Interesting, tell me more!"]
        }

    def greet(self):
        """Greet the user and get their name."""
        print(f"Hello! I'm {self.name}. Type 'bye' to exit.")
        self.user_name = input("What's your name? ")
        print(f"Nice to meet you, {self.user_name}!")
        self.add_to_history("SYSTEM", f"Conversation started with {self.user_name}")

    def get_response(self, user_input):
        """Generate a response to the user input."""
        import random

        if not user_input:
            return "I didn't catch that. Could you try again?"

        user_input = user_input.lower()

        # Handle special commands
        if user_input == "help":
            return self.get_help()
        elif user_input == "history":
            return self.show_history()

        # Check each category of responses
        for category, patterns in self.response_patterns.items():
            for pattern in patterns:
                if pattern in user_input:
                    # Get a random response from the matching category
                    template = random.choice(self.response_templates[category])
                    # Format with user name if needed
                    return template.replace("{user}", self.user_name)

        # Default response if no patterns match
        return random.choice(self.response_templates["default"])

    def add_to_history(self, speaker, text):
        """Add a message to the conversation history."""
        from datetime import datetime
        timestamp = datetime.now().strftime("%H:%M:%S")
        entry = f"[{timestamp}] {speaker}: {text}"
        self.conversation_history.append(entry)
        return len(self.conversation_history)

    def show_history(self):
        """Return the conversation history."""
        if not self.conversation_history:
            return "No conversation history yet."

        history = "\n----- Conversation History -----\n"
        for entry in self.conversation_history:
            history += f"{entry}\n"
        history += "-------------------------------"
        return history

    def get_help(self):
        """Return help information."""
        help_text = f"""
Available Commands:
- 'help': Display this help message
- 'history': Show conversation history
- 'bye': End the conversation

You can also just chat with me normally, {self.user_name}!
"""
        return help_text

    def save_conversation(self):
        """Save the conversation to a file."""
        if not self.conversation_history:
            return "No conversation to save."

        from datetime import datetime
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"chat_with_{self.user_name}_{timestamp}.txt"

        try:
            with open(filename, "w") as f:
                f.write(f"Conversation between {self.name} and {self.user_name}\n")
                f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

                for entry in self.conversation_history:
                    f.write(f"{entry}\n")

            return f"Conversation saved to {filename}"
        except Exception as e:
            return f"Error saving conversation: {str(e)}"

    def run(self):
        """Run the main chatbot loop."""
        self.greet()

        while True:
            user_input = input(f"{self.user_name}> ")
            self.add_to_history(self.user_name, user_input)

            if user_input.lower() == "bye":
                response = f"Goodbye, {self.user_name}! I hope to chat again soon."
                print(f"{self.name}> {response}")
                self.add_to_history(self.name, response)
                break

            if user_input.lower() == "save":
                response = self.save_conversation()
                print(f"{self.name}> {response}")
                self.add_to_history(self.name, response)
                continue

            response = self.get_response(user_input)
            print(f"{self.name}> {response}")
            self.add_to_history(self.name, response)
