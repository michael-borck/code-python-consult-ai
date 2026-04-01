"""
Python AI Integration

Extracted from the companion book.
"""

class AIEnhancedChatbot:
    """A chatbot enhanced with AI capabilities."""

    def __init__(self, name="AI Chatbot", api_key=None):
        """
        Initialize the AI-enhanced chatbot.

        Args:
            name (str): The chatbot's name
            api_key (str, optional): API key for AI services
        """
        self.name = name
        self.user_name = None
        self.conversation_history = []

        # Initialize AI components
        self.message_understanding = MessageUnderstanding(api_key)
        self.conversational_ai = ConversationalAI(
            api_key=api_key,
            system_prompt=f"You are {name}, a helpful assistant. Keep responses concise and friendly."
        )

        # Flag to control AI usage
        self.use_ai = True

    def greet(self):
        """Greet the user and get their name."""
        print(f"Hello! I'm {self.name}, an AI-enhanced chatbot. Type 'bye' to exit.")
        self.user_name = input("What's your name? ")
        print(f"Nice to meet you, {self.user_name}!")
        self.add_to_history("SYSTEM", f"Conversation started with {self.user_name}")

    def add_to_history(self, speaker, text):
        """Add a message to the conversation history."""
        from datetime import datetime
        timestamp = datetime.now().strftime("%H:%M:%S")
        entry = f"[{timestamp}] {speaker}: {text}"
        self.conversation_history.append(entry)

    def get_response(self, user_input):
        """Generate a response to the user input using AI capabilities."""
        # Handle special commands
        if user_input.lower() == "help":
            return self.get_help()
        elif user_input.lower() == "history":
            return self.show_history()
        elif user_input.lower() == "toggle ai":
            self.use_ai = not self.use_ai
            return f"AI features turned {'on' if self.use_ai else 'off'}"

        if not self.use_ai:
            # Fall back to rule-based response if AI is disabled
            return self.get_rule_based_response(user_input)

        try:
            # Use AI to understand the message
            intent_analysis = self.message_understanding.analyze_intent(user_input)
            entities = self.message_understanding.extract_entities(user_input)

            # Log the understanding (in a real system, you might not show this to the user)
            understanding_log = f"Intent: {intent_analysis.get('intent', 'unknown')} ({intent_analysis.get('confidence', 0):.2f})"
            if entities:
                understanding_log += f", Entities: {entities}"
            self.add_to_history("SYSTEM", understanding_log)

            # Get a response from the conversational AI
            ai_response = self.conversational_ai.get_response(user_input)

            return ai_response

        except Exception as e:
            print(f"Error in AI processing: {e}")
            # Fall back to rule-based response if AI fails
            return self.get_rule_based_response(user_input)

    def get_rule_based_response(self, user_input):
        """Generate a response using simple rule-based patterns."""
        user_input = user_input.lower()

        if "hello" in user_input or "hi" in user_input:
            return f"Hello, {self.user_name}! How can I help you today?"
        elif "how are you" in user_input:
            return "I'm doing well, thank you for asking!"
        elif "your name" in user_input:
            return f"My name is {self.name}. I'm an AI-enhanced chatbot."
        elif "bye" in user_input or "goodbye" in user_input:
            return f"Goodbye, {self.user_name}! It was nice chatting with you."
        else:
            return "I'm not sure how to respond to that. Can you try asking something else?"

    def show_history(self):
        """Show the conversation history."""
        if not self.conversation_history:
            return "No conversation history yet."

        history = "\n----- Conversation History -----\n"
        for entry in self.conversation_history:
            history += f"{entry}\n"
        history += "-------------------------------"
        return history

    def get_help(self):
        """Get help information."""
        help_text = f"""
Available Commands:
- 'help': Display this help message
- 'history': Show conversation history
- 'toggle ai': Turn AI features on/off
- 'bye': End the conversation

You can also just chat with me normally, {self.user_name}!
"""
        return help_text

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

            response = self.get_response(user_input)
            print(f"{self.name}> {response}")
            self.add_to_history(self.name, response)
