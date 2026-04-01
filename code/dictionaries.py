"""
Dictionaries - organising Data with Key-Value Pairs

Extracted from the companion book.
"""

import random

# Using dictionaries for more sophisticated response patterns
response_patterns = {
    "greetings": ["hello", "hi", "hey", "howdy", "hola", "morning", "evening"],
    "farewells": ["bye", "goodbye", "see you", "cya", "farewell", "exit"],
    "gratitude": ["thanks", "thank you", "appreciate", "grateful"],
    "bot_questions": ["who are you", "what are you", "your name", "your purpose"],
    "user_questions": ["how are you", "what's up", "how do you feel"],
    "capabilities": ["what can you do", "help", "functions", "abilities", "commands"]
}

response_templates = {
    "greetings": [
        "Hello there! How can I help you today?",
        "Hi! Nice to chat with you!",
        "Hey! How's your day going?",
        "Greetings! What's on your mind?"
    ],
    "farewells": [
        "Goodbye! Come back soon!",
        "See you later! Have a great day!",
        "Until next time! Take care!",
        "Farewell! It was nice chatting with you!"
    ],
    "gratitude": [
        "You're welcome!",
        "Happy to help!",
        "My pleasure!",
        "No problem at all!"
    ],
    "bot_questions": [
        f"I'm PyBot, a simple chatbot built with Python!",
        "I'm a demonstration chatbot for the Python Jumpstart book.",
        "I'm your friendly Python-powered conversation partner!"
    ],
    "user_questions": [
        "I'm functioning well, thanks for asking!",
        "I'm here and ready to chat!",
        "I'm operational and at your service!"
    ],
    "capabilities": [
        "I can chat about basic topics, remember our conversation, and give responses based on patterns I recognise.",
        "Try asking me who I am, say hello, or just chat naturally!",
        "I can respond to greetings, questions about myself, and basic conversation. I'm also learning new tricks!"
    ],
    "unknown": [
        "I'm not sure I understand. Can you rephrase that?",
        "Hmm, I'm still learning and don't quite understand that.",
        "That's beyond my current capabilities, but I'm always learning!",
        "Interesting, tell me more about that."
    ]
}

# User stats dictionary to track interaction metrics
user_stats = {
    "message_count": 0,
    "question_count": 0,
    "greeting_count": 0,
    "command_count": 0,
    "start_time": None,
    "topics": {}  # Count topics discussed
}

def get_response(user_input):
    """Get a response using dictionary-based pattern matching."""
    user_input = user_input.lower().strip()

    # Update stats
    user_stats["message_count"] += 1
    if user_input.endswith("?"):
        user_stats["question_count"] += 1

    # Check for special commands
    if user_input == "stats":
        user_stats["command_count"] += 1
        return f"""
Conversation Stats:
- Messages sent: {user_stats['message_count']}
- Questions asked: {user_stats['question_count']}
- Greetings: {user_stats['greeting_count']}
- Commands used: {user_stats['command_count']}
- Topics mentioned: {', '.join(user_stats['topics'].keys()) if user_stats['topics'] else 'None'}
        """.strip()

    # Check for patterns in our response dictionary
    for category, patterns in response_patterns.items():
        for pattern in patterns:
            if pattern in user_input:
                # Update stats for this topic/category
                if category in user_stats["topics"]:
                    user_stats["topics"][category] += 1
                else:
                    user_stats["topics"][category] = 1

                if category == "greetings":
                    user_stats["greeting_count"] += 1

                # Return a random response from the matching category
                return random.choice(response_templates[category])

    # No pattern matched, return an unknown response
    return random.choice(response_templates["unknown"])

# Main chat loop
bot_name = "PyBot"
print(f"Hello! I'm {bot_name}. Type 'bye' to exit or 'stats' for conversation statistics.")
user_name = input("What's your name? ").strip()
print(f"Nice to meet you, {user_name}!")

from datetime import datetime
user_stats["start_time"] = datetime.now()

conversation_history = []

def save_to_history(speaker, text):
    """Save an utterance to conversation history."""
    timestamp = datetime.now().strftime("%H:%M:%S")
    conversation_history.append({
        "speaker": speaker,
        "text": text,
        "timestamp": timestamp
    })

def show_history():
    """Display the conversation history."""
    print("\n----- Conversation History -----")
    for entry in conversation_history:
        print(f"[{entry['timestamp']}] {entry['speaker']}: {entry['text']}")
    print("-------------------------------\n")

# Save initial greeting
save_to_history(bot_name, f"Nice to meet you, {user_name}!")

while True:
    user_input = input(f"{user_name}> ")
    save_to_history(user_name, user_input)

    if user_input.lower() in ["bye", "exit", "quit", "goodbye"]:
        duration = datetime.now() - user_stats["start_time"]
        minutes = int(duration.total_seconds() // 60)
        seconds = int(duration.total_seconds() % 60)

        response = f"Goodbye, {user_name}! We chatted for {minutes} minutes and {seconds} seconds."
        print(f"{bot_name}> {response}")
        save_to_history(bot_name, response)
        break
    elif user_input.lower() == "history":
        show_history()
        continue

    response = get_response(user_input)
    print(f"{bot_name}> {response}")
    save_to_history(bot_name, response)
