"""
Testing - Ensuring Your Code Works as Intended

Extracted from the companion book.
"""

import unittest
from unittest.mock import patch

# Import your chatbot or include minimal implementation for testing
class Chatbot:
    def __init__(self, name="PyBot"):
        self.name = name
        self.user_name = None
        self.conversation_history = []
        self.response_patterns = {
            "greetings": ["hello", "hi", "hey"],
            "farewells": ["bye", "goodbye", "exit"],
            "help": ["help", "commands", "options"]
        }
        self.response_templates = {
            "greetings": ["Hello there!", "Hi! Nice to chat with you!"],
            "farewells": ["Goodbye!", "See you later!"],
            "help": ["Here are my commands...", "I can help with..."],
            "default": ["I'm not sure about that.", "Can you tell me more?"]
        }

    def get_response(self, user_input):
        """Generate a response based on user input."""
        if not user_input:
            return "I didn't catch that. Can you try again?"

        user_input = user_input.lower()

        # Check each category of responses
        for category, patterns in self.response_patterns.items():
            for pattern in patterns:
                if pattern in user_input:
                    # In a real implementation, you might pick randomly
                    # but for testing, we'll use the first template
                    return self.response_templates[category][0]

        # Default response if no patterns match
        return self.response_templates["default"][0]

    def add_to_history(self, speaker, text):
        """Add a message to conversation history."""
        self.conversation_history.append(f"{speaker}: {text}")
        return len(self.conversation_history)

class TestChatbot(unittest.TestCase):
    def setUp(self):
        """Create a fresh chatbot for each test."""
        self.chatbot = Chatbot(name="TestBot")

    def test_initialization(self):
        """Test that chatbot initializes with correct default values."""
        self.assertEqual(self.chatbot.name, "TestBot")
        self.assertIsNone(self.chatbot.user_name)
        self.assertEqual(len(self.chatbot.conversation_history), 0)
        self.assertIn("greetings", self.chatbot.response_patterns)
        self.assertIn("farewells", self.chatbot.response_templates)

    def test_greeting_response(self):
        """Test that chatbot responds to greetings."""
        response = self.chatbot.get_response("hello there")
        self.assertEqual(response, "Hello there!")

        response = self.chatbot.get_response("HI everyone")  # Testing case insensitivity
        self.assertEqual(response, "Hello there!")

    def test_farewell_response(self):
        """Test that chatbot responds to farewells."""
        response = self.chatbot.get_response("goodbye")
        self.assertEqual(response, "Goodbye!")

    def test_default_response(self):
        """Test that chatbot gives default response for unknown input."""
        response = self.chatbot.get_response("blah blah random text")
        self.assertEqual(response, "I'm not sure about that.")

    def test_empty_input(self):
        """Test that chatbot handles empty input."""
        response = self.chatbot.get_response("")
        self.assertEqual(response, "I didn't catch that. Can you try again?")

    def test_conversation_history(self):
        """Test that messages are added to conversation history."""
        initial_length = len(self.chatbot.conversation_history)
        new_length = self.chatbot.add_to_history("User", "Test message")

        # Check that length increased by 1
        self.assertEqual(new_length, initial_length + 1)

        # Check that message was added correctly
        self.assertEqual(self.chatbot.conversation_history[-1], "User: Test message")

    def test_multiple_patterns_in_input(self):
        """Test that chatbot handles input with multiple patterns."""
        # If input contains both greeting and farewell, it should match the first one found
        response = self.chatbot.get_response("hello and goodbye")
        self.assertEqual(response, "Hello there!")

# Run the tests
if __name__ == '__main__':
    unittest.main()
