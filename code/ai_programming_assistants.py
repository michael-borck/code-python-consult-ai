"""
AI Programming Assistants

Extracted from the companion book.
"""

# Original simple chatbot implementation
class SimpleBot:
    def __init__(self, name):
        self.name = name
        self.responses = {
            "hello": "Hi there!",
            "how are you": "I'm good, thanks!",
            "bye": "Goodbye!"
        }

    def get_response(self, message):
        for key, response in self.responses.items():
            if key in message.lower():
                return response
        return "I don't understand."

# AI-suggested improved version
class EnhancedBot:
    def __init__(self, name):
        self.name = name
        self.user_name = None
        self.conversation_start = datetime.now()
        self.message_count = 0
        self.responses = {
            "greeting": ["Hi there!", "Hello!", "Greetings!"],
            "farewell": ["Goodbye!", "See you later!", "Bye for now!"],
            "inquiry": ["I'm just a chatbot.", "I'm doing well!", "I exist to chat!"],
            "default": ["I don't understand.", "Could you rephrase that?", "I'm not sure what you mean."]
        }
        self.patterns = {
            "greeting": ["hello", "hi", "hey", "greetings"],
            "farewell": ["bye", "goodbye", "see you", "farewell"],
            "inquiry": ["how are you", "what are you", "who are you"]
        }
        self.conversation_history = []

    def get_response(self, message):
        self.message_count += 1
        self.conversation_history.append(f"User: {message}")

        # Extract user name if not already known
        if self.user_name is None and "my name is" in message.lower():
            name_match = re.search(r'my name is (\w+)', message, re.IGNORECASE)
            if name_match:
                self.user_name = name_match.group(1)
                response = f"Nice to meet you, {self.user_name}!"
                self.conversation_history.append(f"{self.name}: {response}")
                return response

        # Match patterns
        for category, patterns in self.patterns.items():
            for pattern in patterns:
                if pattern in message.lower():
                    response = random.choice(self.responses[category])

                    # Personalize if user name is known
                    if self.user_name and category == "greeting":
                        response = response.replace("!", f", {self.user_name}!")

                    self.conversation_history.append(f"{self.name}: {response}")
                    return response

        # Default response
        response = random.choice(self.responses["default"])
        self.conversation_history.append(f"{self.name}: {response}")
        return response
