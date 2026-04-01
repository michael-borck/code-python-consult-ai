"""
How to Run Python Code

Extracted from the companion book.
"""

# In a Jupyter notebook cell
from chatbot.main import Chatbot
import ipywidgets as widgets
from IPython.display import display, clear_output

# Create a chatbot instance
bot = Chatbot(name="JupyterBot")

# Create input and display widgets
messages = []
output = widgets.Output()
text_input = widgets.Text(description="You:", placeholder="Type a message...")
send_button = widgets.Button(description="Send")

# Display interface
display(output)
input_box = widgets.HBox([text_input, send_button])
display(input_box)

# Define interaction behaviour
def on_send_clicked(b):
    user_input = text_input.value
    if not user_input:
        return

    # Clear input box
    text_input.value = ""

    # Add user message to display
    messages.append(f"You: {user_input}")

    # Get bot response
    bot_response = bot.get_response(user_input)
    messages.append(f"JupyterBot: {bot_response}")

    # Update display
    with output:
        clear_output()
        for message in messages:
            print(message)

# Connect button click to handler
send_button.on_click(on_send_clicked)
