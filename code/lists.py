"""
Lists - organising Collections of Data

Extracted from the companion book.
"""

import datetime
from collections import deque
from typing import Dict, List, Any, Optional

class ChatHistory:
    def __init__(self, max_size: int = 100):
        """Initialize chat history with a maximum size.

        Args:
            max_size: Maximum number of messages to store (oldest removed first)
        """
        # Using deque for efficient appending and popping from both ends
        self.messages = deque(maxlen=max_size)

    def add_message(self, speaker: str, content: str,
                   timestamp: Optional[datetime.datetime] = None) -> None:
        """Add a message to the history.

        Args:
            speaker: Name of the message sender
            content: The message text
            timestamp: Optional timestamp (defaults to current time)
        """
        if timestamp is None:
            timestamp = datetime.datetime.now()

        message = {
            "timestamp": timestamp,
            "speaker": speaker,
            "content": content
        }

        self.messages.append(message)

    def get_recent(self, n: int = 5) -> List[Dict[str, Any]]:
        """Get the n most recent messages.

        Args:
            n: Number of messages to retrieve

        Returns:
            List of message dictionaries
        """
        # Convert to list for easier slicing
        history_list = list(self.messages)
        # Return at most n items, starting from the end
        return history_list[-min(n, len(history_list)):]

    def search(self, keyword: str) -> List[Dict[str, Any]]:
        """Search for messages containing the keyword.

        Args:
            keyword: Term to search for (case-insensitive)

        Returns:
            List of matching message dictionaries
        """
        keyword = keyword.lower()
        return [msg for msg in self.messages
                if keyword in msg["content"].lower()]

    def get_context(self, n: int = 3) -> str:
        """Get recent messages formatted as context for AI responses.

        Args:
            n: Number of recent messages to include

        Returns:
            Formatted string with recent conversation
        """
        recent = self.get_recent(n)

        context = []
        for msg in recent:
            timestamp = msg["timestamp"].strftime("%H:%M:%S")
            context.append(f"[{timestamp}] {msg['speaker']}: {msg['content']}")

        return "\n".join(context)

    def generate_summary(self) -> Dict[str, Any]:
        """Generate a statistical summary of the conversation.

        Returns:
            Dictionary with conversation metrics
        """
        if not self.messages:
            return {"message_count": 0}

        # Get all messages as a list for analysis
        all_msgs = list(self.messages)

        # Basic count statistics
        speakers = {}
        word_count = 0

        for msg in all_msgs:
            speaker = msg["speaker"]
            speakers[speaker] = speakers.get(speaker, 0) + 1
            word_count += len(msg["content"].split())

        # Time statistics
        if len(all_msgs) > 1:
            start_time = all_msgs[0]["timestamp"]
            end_time = all_msgs[-1]["timestamp"]
            duration = (end_time - start_time).total_seconds()
        else:
            duration = 0

        return {
            "message_count": len(all_msgs),
            "speaker_counts": speakers,
            "word_count": word_count,
            "duration_seconds": duration,
            "messages_per_minute": (len(all_msgs) * 60 / duration) if duration > 0 else 0
        }


# Example usage:
def demo_chat_history():
    history = ChatHistory(max_size=1000)

    # Add some sample messages
    history.add_message("User", "Hello, chatbot!")
    history.add_message("Bot", "Hello! How can I help you today?")
    history.add_message("User", "I'm looking for information about Python lists.")
    history.add_message("Bot", "Lists are ordered, mutable collections in Python.")
    history.add_message("User", "Can you give me an example?")

    # Get recent messages
    print("Recent messages:")
    for msg in history.get_recent(3):
        print(f"{msg['speaker']}: {msg['content']}")

    # Search for messages
    print("\nSearch results for 'python':")
    for msg in history.search("python"):
        print(f"{msg['speaker']}: {msg['content']}")

    # Get conversation context
    print("\nConversation context:")
    print(history.get_context())

    # Generate summary
    print("\nConversation summary:")
    summary = history.generate_summary()
    for key, value in summary.items():
        print(f"{key}: {value}")

# Run the demo
# demo_chat_history()
