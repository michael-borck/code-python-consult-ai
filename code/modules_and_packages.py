"""
Modules and Packages - organising Your Python Code

Extracted from the companion book.
"""

"""Functions for managing conversation history."""
import datetime
import os

class HistoryManager:
    def __init__(self):
        """Initialize with empty history."""
        self.conversation_history = []

    def add_to_history(self, speaker, text):
        """Add a message to conversation history."""
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        entry = f"[{timestamp}] {speaker}: {text}"
        self.conversation_history.append(entry)
        return len(self.conversation_history)

    def show_history(self):
        """Return formatted conversation history."""
        if not self.conversation_history:
            return "No conversation history yet."

        history = "\n----- Conversation History -----\n"
        for entry in self.conversation_history:
            history += f"{entry}\n"
        history += "-------------------------------"
        return history

    def save_conversation(self, user_name, bot_name):
        """Save conversation history to a file."""
        if not self.conversation_history:
            return "No conversation to save."

        # Create a timestamped filename
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"chat_with_{user_name}_{timestamp}.txt"

        try:
            with open(filename, "w") as f:
                f.write(f"Conversation between {bot_name} and {user_name}\n")
                f.write(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

                for entry in self.conversation_history:
                    f.write(f"{entry}\n")

            return f"Conversation saved to {filename}"
        except Exception as e:
            return f"Error saving conversation: {str(e)}"

    def load_conversation(self, filename):
        """Load a previous conversation from a file."""
        try:
            with open(filename, "r") as f:
                content = f.read()
            return content
        except FileNotFoundError:
            return f"Could not find file: {filename}"
        except Exception as e:
            return f"Error loading conversation: {str(e)}"
