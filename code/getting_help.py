"""
Getting Help with Python

Extracted from the companion book.
"""

class DebuggableChatbot(Chatbot):
    """An extension of the Chatbot class with debugging capabilities."""

    def __init__(self, name="DebugBot", debug=False):
        """Initialize with optional debug mode."""
        super().__init__(name)
        self.debug = debug

    def get_response(self, user_input):
        """Get response with debug information if debug mode is on."""
        if self.debug:
            print(f"DEBUG: Processing input: '{user_input}'")
            print(f"DEBUG: Current response patterns: {self.response_patterns.keys()}")

        # Standard processing
        user_input = user_input.lower()

        # Match patterns
        for category, patterns in self.response_patterns.items():
            for pattern in patterns:
                if pattern in user_input:
                    if self.debug:
                        print(f"DEBUG: Matched pattern '{pattern}' in category '{category}'")

                    # Get response from standard method
                    response = super().get_response(user_input)

                    if self.debug:
                        print(f"DEBUG: Selected response: '{response}'")

                    return response

        if self.debug:
            print("DEBUG: No pattern match found, using default response")

        return super().get_response(user_input)
