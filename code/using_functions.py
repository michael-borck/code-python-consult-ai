"""
Using Functions - Python's Built-in Powertools

Extracted from the companion book.
"""

# Enhanced chatbot with help function
bot_name = "PyBot"

print(f"Hello! I'm {bot_name}, your Python assistant.")
user_name = input("What's your name? ")
print(f"Nice to meet you, {user_name}!")

while True:
    user_input = input(f"\n{user_name}> ")
    user_input = user_input.lower()

    if user_input == "bye":
        print(f"{bot_name}> Goodbye, {user_name}! It was nice talking with you.")
        break

    elif user_input.startswith("help("):
        # Extract the function name from help(function_name)
        try:
            function_name = user_input[5:-1].strip()  # Remove "help(" and ")"
            print(f"{bot_name}> Let me tell you about the {function_name} function:")
            # We use the built-in help system but capture the output
            help(eval(function_name))  # This is advanced - we'll explain eval later
        except:
            print(f"{bot_name}> I'm sorry, I couldn't find information about that function.")

    elif user_input == "help":
        print(f"{bot_name}> Here are some built-in functions you can ask about:")
        print("  print, input, len, int, str, float, bool, max, min, sum, abs, round, pow")
        print("Use help(function_name) to learn about a specific function.")

    elif "age" in user_input:
        print(f"{bot_name}> I was created today!")

    elif "name" in user_input:
        print(f"{bot_name}> My name is {bot_name}.")

    elif "calculate" in user_input:
        print(f"{bot_name}> I can do math! Try asking me to calculate something.")
        math_question = input(f"{user_name}> ")

        if "+" in math_question:
            parts = math_question.split("+")
            if len(parts) == 2:
                try:
                    num1 = int(parts[0].strip())
                    num2 = int(parts[1].strip())
                    result = num1 + num2
                    print(f"{bot_name}> The answer is {result}")
                except ValueError:
                    print(f"{bot_name}> Sorry, I couldn't understand those numbers.")
        else:
            print(f"{bot_name}> I can only handle addition for now. Stay tuned for updates!")

    else:
        print(f"{bot_name}> I'm still learning and don't know how to respond to that yet.")
