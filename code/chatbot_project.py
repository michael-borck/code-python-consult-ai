"""
---

Extracted from the companion book.
"""

# Enhance your chatbot with AI capabilities
import os
from dotenv import load_dotenv
import openai  # You'll need to pip install openai

# Load API key from environment variable
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

class AIEnhancedChatbot(Chatbot):
    """A chatbot enhanced with AI capabilities."""
    
    def __init__(self, name="AI-PyBot"):
        super().__init__(name)
        self.ai_mode = False
        self.conversation_context = []
    
    def toggle_ai_mode(self):
        """Toggle between rule-based and AI-powered responses."""
        self.ai_mode = not self.ai_mode
        return f"AI mode is now {'on' if self.ai_mode else 'off'}"
    
    def get_ai_response(self, user_input):
        """Get a response from the OpenAI API."""
        # Add to conversation context
        self.conversation_context.append({"role": "user", "content": user_input})
        
        try:
            # Get response from OpenAI
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": f"You are {self.name}, a helpful assistant chatbot. Respond in a friendly, concise manner."},
                    *self.conversation_context
                ]
            )
            
            # Extract and save the assistant's response
            ai_response = response.choices[0].message["content"]
            self.conversation_context.append({"role": "assistant", "content": ai_response})
            
            # Keep context window manageable (retain last 10 exchanges)
            if len(self.conversation_context) > 20:
                self.conversation_context = self.conversation_context[-20:]
                
            return ai_response
            
        except Exception as e:
            return f"AI error: {str(e)}"
    
    def get_response(self, user_input):
        """Get a response using either rule-based or AI approach."""
        if user_input.lower() == "ai mode":
            return self.toggle_ai_mode()
            
        if self.ai_mode:
            return self.get_ai_response(user_input)
        else:
            return super().get_response(user_input)
