"""
---

Extracted from the companion book.
"""

import os
from dotenv import load_dotenv
import openai

# Load API key from environment variable
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

class IntentionalPrompter:
    """
    A class that crafts intentional prompts for AI interactions
    based on conversation context and user inputs.
    """

    def __init__(self):
        self.prompt_templates = {
            "greeting": "The user has greeted the chatbot with: '{user_input}'. "
                        "Respond in a friendly manner. Keep the response brief and personalized.",

            "question": "The user has asked: '{user_input}'. "
                        "Provide a helpful, accurate, and concise response. "
                        "If the question is about Python programming, include a small code example if relevant.",

            "clarification": "The user's message: '{user_input}' is unclear or ambiguous. "
                             "Ask for clarification in a friendly way. Suggest possible interpretations.",

            "technical": "The user is asking about a technical Python concept: '{user_input}'. "
                         "Explain it clearly with a simple example. "
                         "Define any technical terms. Keep the explanation beginner-friendly.",

            "code_help": "The user needs help with this code: '{user_input}'. "
                         "First identify any issues. Then provide a corrected version. "
                         "Finally, explain what was wrong and the principles behind the fix."
        }

    def detect_intent(self, user_input):
        """Determine the general intent of the user's message."""
        user_input = user_input.lower()

        # Simple intent detection based on keywords and patterns
        if any(greeting in user_input for greeting in ["hello", "hi", "hey", "greetings"]):
            return "greeting"

        if user_input.endswith("?") or any(q in user_input for q in ["how", "what", "why", "when", "where", "who"]):
            return "question"

        if "code" in user_input or "python" in user_input or "function" in user_input:
            if "help" in user_input or "fix" in user_input or "debug" in user_input:
                return "code_help"
            return "technical"

        return "clarification"  # Default if we can't clearly determine intent

    def craft_prompt(self, user_input, conversation_history=None):
        """
        Craft an intentional prompt based on the user's input and conversation history.
        """
        intent = self.detect_intent(user_input)
        base_prompt = self.prompt_templates[intent].format(user_input=user_input)

        # Enhance prompt with conversation context if available
        if conversation_history and len(conversation_history) > 0:
            context = "\nRecent conversation context:\n"
            # Include up to 3 most recent exchanges
            for i, exchange in enumerate(conversation_history[-3:]):
                context += f"User: {exchange['user']}\n"
                context += f"Bot: {exchange['bot']}\n"
            base_prompt = context + "\n" + base_prompt

        # Add specific instructions based on intent
        if intent == "technical":
            base_prompt += "\nInclude at least one practical example. Mention common pitfalls."
        elif intent == "code_help":
            base_prompt += "\nMake sure to explain why the solution works, not just what the solution is."

        return base_prompt

class EnhancedAIChatbot:
    """
    Chatbot enhanced with intentional prompting for better AI interactions.
    """

    def __init__(self, name="PyBot"):
        self.name = name
        self.conversation_history = []
        self.prompter = IntentionalPrompter()

        # Initialize OpenAI client
        load_dotenv()
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.openai = openai
        self.openai.api_key = self.api_key

    def add_to_history(self, user_input, bot_response):
        """Add an exchange to the conversation history."""
        self.conversation_history.append({
            "user": user_input,
            "bot": bot_response
        })

        # Keep history at a reasonable size
        if len(self.conversation_history) > 10:
            self.conversation_history.pop(0)

    def get_ai_response(self, user_input):
        """
        Get a response from the AI service using intentional prompting.
        """
        if not self.api_key:
            return "AI services are not configured. Please set up your API key."

        try:
            # Craft an intentional prompt
            prompt = self.prompter.craft_prompt(user_input, self.conversation_history)

            # Get response from OpenAI
            response = self.openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": f"You are {self.name}, a friendly and helpful assistant for Python programming."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=150,
                temperature=0.7
            )

            # Extract and return the response content
            return response.choices[0].message["content"].strip()

        except Exception as e:
            return f"Sorry, I encountered an issue while processing your request: {str(e)}"

    def chat(self):
        """Run an interactive chat session."""
        print(f"{self.name}: Hello! I'm {self.name}, your Python assistant. How can I help you today?")

        while True:
            user_input = input("You: ")

            if user_input.lower() in ["exit", "quit", "bye"]:
                print(f"{self.name}: Goodbye! Happy coding!")
                break

            # Get response using intentional prompting
            response = self.get_ai_response(user_input)
            print(f"{self.name}: {response}")

            # Update conversation history
            self.add_to_history(user_input, response)
