"""
AI Assistance Tips

Extracted from the companion book.
"""

class AdvancedAIChatbot:
    """
    Sophisticated chatbot that combines rule-based responses with selective AI usage.
    Includes contextual memory, sentiment analysis, and adaptive response generation.
    """

    def __init__(self, name="AI-PyBot", openai_api_key=None):
        self.name = name
        self.user_name = None
        self.context_memory = ContextualMemory()

        # Initialize response templates
        self.response_templates = {
            "greeting": ["Hello!", "Hi there!", "Hey! How can I help?"],
            "greeting_responses": ["Hello!", "Hi there!", "Hey! How can I help?"],
            "farewell": ["bye", "goodbye", "see you", "exit", "quit"],
            "farewell_responses": ["Goodbye!", "See you later!", "Until next time!"],
            "thanks": ["thanks", "thank you", "appreciate"],
            "thanks_responses": ["You're welcome!", "Happy to help!", "No problem!"],
            "name": ["your name", "who are you", "what are you called"],
            "name_responses": [f"I'm {name}, your assistant.", f"My name is {name}.", f"You can call me {name}."]
        }

        # Initialize selective AI usage manager
        if openai_api_key:
            self.ai_manager = SelectiveAIManager(openai_api_key)
            self.hybrid_response = HybridResponseSystem(openai_api_key, self.response_templates, name)
            self.ai_available = True
        else:
            self.ai_available = False

        # Initialize sentiment tracker
        self.sentiment_tracker = {
            "positive": 0,
            "negative": 0,
            "questions": 0,
            "total_interactions": 0
        }

    def process_message(self, user_input):
        """Process user message and generate appropriate response."""
        # Update interaction counter
        self.sentiment_tracker["total_interactions"] += 1

        # Extract user name if first interaction
        if not self.user_name and "my name is" in user_input.lower():
            name_match = re.search(r"my name is (\w+)", user_input, re.IGNORECASE)
            if name_match:
                self.user_name = name_match.group(1)
                self.context_memory.extract_fact("user_name", self.user_name)
                return f"Nice to meet you, {self.user_name}! How can I help you today?"

        # Update question counter
        if "?" in user_input:
            self.sentiment_tracker["questions"] += 1

        # Basic sentiment analysis
        positive_words = ["good", "great", "awesome", "excellent", "happy", "like", "love"]
        negative_words = ["bad", "terrible", "awful", "unhappy", "hate", "dislike", "worst"]

        for word in positive_words:
            if word in user_input.lower():
                self.sentiment_tracker["positive"] += 1
                break

        for word in negative_words:
            if word in user_input.lower():
                self.sentiment_tracker["negative"] += 1
                break

        # Choose response strategy
        if self.ai_available and self.ai_manager.should_use_ai(user_input, self.context_memory.conversation_history):
            # Use hybrid response system for complex queries
            response = self.hybrid_response.get_response(user_input)
        else:
            # Use rule-based response for simple queries
            response = self._get_rule_based_response(user_input)

        # Update conversation memory
        self.context_memory.add_exchange(user_input, response)
        return response

    def _get_rule_based_response(self, user_input):
        """Generate a rule-based response."""
        user_input = user_input.lower()

        # Check each response category
        for intent, patterns in self.response_templates.items():
            if intent.endswith("_responses"):
                continue  # Skip response arrays

            for pattern in patterns:
                if pattern in user_input:
                    responses = self.response_templates.get(f"{intent}_responses", ["I understand."])
                    response = random.choice(responses)

                    # Personalize if user name is known
                    if self.user_name and intent == "greeting":
                        response = response.replace("!", f", {self.user_name}!")

                    return response

        # Default responses
        default_responses = [
            "I'm not sure I understand. Could you rephrase that?",
            "I'm still learning. Can you tell me more?",
            "Interesting. Could you elaborate on that?",
            "I'm not quite sure how to respond to that."
        ]
        return random.choice(default_responses)

    def get_conversation_stats(self):
        """Get statistics about the conversation."""
        total = self.sentiment_tracker["total_interactions"]
        if total == 0:
            return "We haven't had much of a conversation yet."

        stats = {
            "total_messages": total,
            "question_percentage": (self.sentiment_tracker["questions"] / total) * 100 if total > 0 else 0,
            "positive_sentiment": (self.sentiment_tracker["positive"] / total) * 100 if total > 0 else 0,
            "negative_sentiment": (self.sentiment_tracker["negative"] / total) * 100 if total > 0 else 0,
        }

        return f"""Conversation Statistics:
- Total messages: {stats['total_messages']}
- Questions asked: {self.sentiment_tracker['questions']} ({stats['question_percentage']:.1f}%)
- Positive sentiment: {stats['positive_sentiment']:.1f}%
- Negative sentiment: {stats['negative_sentiment']:.1f}%
"""
