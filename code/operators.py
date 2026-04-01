"""
Operators - The Building Blocks of Python Logic

Extracted from the companion book.
"""

def advanced_logic_chatbot():
    """A chatbot with more sophisticated decision logic using operators."""
    bot_name = "PyBot"

    print(f"\n{bot_name}> Hello! I'm {bot_name}, your Python learning assistant.")
    user_name = input("You> ").strip()

    # Track conversation context
    question_count = 0
    greeting_count = 0
    python_mentioned = False
    last_topic = None

    print(f"\n{bot_name}> Nice to meet you, {user_name}! Ask me about Python or programming.")

    while True:
        user_input = input(f"\n{user_name}> ").strip().lower()

        # Exit check with confirmation for long conversations
        if user_input == "bye":
            if question_count > 3:
                print(f"\n{bot_name}> You've asked {question_count} questions! Are you sure you want to leave?")
                confirm = input(f"{user_name}> ").strip().lower()
                if confirm in ["yes", "y"]:
                    print(f"\n{bot_name}> Goodbye, {user_name}! Hope I was helpful!")
                    break
                else:
                    print(f"\n{bot_name}> Great! Let's continue our conversation.")
                    continue
            else:
                print(f"\n{bot_name}> Goodbye, {user_name}! Come back if you have more questions.")
                break

        # Update conversation context
        if "?" in user_input:
            question_count += 1

        if any(greeting in user_input for greeting in ["hello", "hi", "hey"]):
            greeting_count += 1

        if "python" in user_input:
            python_mentioned = True

        # Response generation with complex conditions
        if greeting_count > 2 and len(user_input) < 10:
            # Repeated short greetings
            print(f"\n{bot_name}> We've exchanged greetings already. Is there something")
            print(f"{bot_name}> specific I can help you with?")

        elif "python" in user_input and "learn" in user_input:
            # Questions about learning Python
            print(f"\n{bot_name}> Learning Python is a great choice! The key concepts to master are:")
            print(f"{bot_name}> 1. Variables and data types")
            print(f"{bot_name}> 2. Control structures (if statements, loops)")
            print(f"{bot_name}> 3. Functions and modules")
            print(f"{bot_name}> 4. Object-oriented programming")
            last_topic = "learning"

        elif "operator" in user_input and "?" in user_input:
            # Questions about operators
            print(f"\n{bot_name}> Python has several types of operators:")
            print(f"{bot_name}> - Arithmetic: +, -, *, /, //, %, **")
            print(f"{bot_name}> - Comparison: ==, !=, <, >, <=, >=")
            print(f"{bot_name}> - Logical: and, or, not")
            print(f"{bot_name}> - Membership: in, not in")
            last_topic = "operators"

        elif last_topic == "operators" and "example" in user_input:
            # Follow-up question about operators
            print(f"\n{bot_name}> Here's an example combining different operators:")
            print(f"{bot_name}> age = 25")
            print(f"{bot_name}> is_adult = age >= 18  # True")
            print(f"{bot_name}> can_retire = age >= 65  # False")
            print(f"{bot_name}> needs_id = is_adult and not can_retire  # True")

        elif question_count >= 5 and not user_input.endswith("?"):
            # Many questions but current input isn't a question
            print(f"\n{bot_name}> You've asked {question_count} questions so far! Do you have")
            print(f"{bot_name}> another question? I'm here to help.")

        elif "thanks" in user_input or "thank you" in user_input:
            # Gratitude
            print(f"\n{bot_name}> You're welcome, {user_name}! I'm happy to assist.")
            if question_count > 0:
                print(f"{bot_name}> You've asked {question_count} questions in our conversation.")

        elif len(user_input) > 50:
            # Very long input
            print(f"\n{bot_name}> That's quite detailed! Let me break this down...")
            words = user_input.split()
            print(f"{bot_name}> Your message had {len(words)} words. To help you better,")
            print(f"{bot_name}> could you ask more specific, focused questions?")

        else:
            # Default response based on conversation context
            if python_mentioned:
                print(f"\n{bot_name}> Python is a versatile language. What specific")
                print(f"{bot_name}> aspect of Python are you interested in?")
            else:
                print(f"\n{bot_name}> I'm designed to help with Python programming.")
                print(f"{bot_name}> Try asking me about Python concepts, operators, or syntax!")

    print("\nChat session ended.")

# Run the advanced chatbot (commented out to avoid execution)
# advanced_logic_chatbot()
