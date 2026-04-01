"""
Making Decisions - Controlling Your Program's Flow

Extracted from the companion book.
"""

def context_aware_chatbot():
    """A more sophisticated chatbot that maintains conversation context."""
    bot_name = "PyBot"

    # Initialize conversation state
    context = {
        "user_name": "",
        "topics_discussed": set(),
        "question_count": 0,
        "mood": "neutral",  # bot's mood: can be "happy", "neutral", or "tired"
        "last_topic": None
    }

    # Helper function to update context
    def update_context(user_input):
        # Track topics
        if "python" in user_input.lower():
            context["topics_discussed"].add("python")
        if "weather" in user_input.lower():
            context["topics_discussed"].add("weather")
        if "music" in user_input.lower():
            context["topics_discussed"].add("music")

        # Track questions
        if "?" in user_input:
            context["question_count"] += 1

        # Update mood (bot gets "tired" after many questions)
        if context["question_count"] > 5:
            context["mood"] = "tired"

        # Track last topic mentioned
        for topic in ["python", "weather", "music", "movies", "books"]:
            if topic in user_input.lower():
                context["last_topic"] = topic
                break

    # Main response function
    def get_contextual_response(user_input):
        user_input = user_input.lower()
        update_context(user_input)

        # Special case for greeting - depends on bot's mood
        if "hello" in user_input or "hi" in user_input:
            if context["mood"] == "happy":
                return f"Hello {context['user_name']}! It's wonderful to see you! How can I help you today?"
            elif context["mood"] == "tired":
                return f"Hi {context['user_name']}... You've asked quite a few questions. I'll try to keep up!"
            else:
                return f"Hello {context['user_name']}! How can I help you today?"

        # Check for questions about previous topics
        if "tell me more" in user_input and context["last_topic"]:
            topic = context["last_topic"]
            if topic == "python":
                return "Python is a versatile language used for web development, data analysis, AI, and more. What specific aspect interests you?"
            elif topic == "weather":
                return "Weather is the state of the atmosphere, including temperature, humidity, wind, etc. Any specific weather phenomenon you're curious about?"
            elif topic == "music":
                return "Music comes in countless genres from classical to electronic. Do you have a favourite style?"
            else:
                return f"You wanted to know more about {topic}? What specific aspect interests you?"

        # Check for topic switching
        prev_topics = context["topics_discussed"].copy()
        update_context(user_input)  # This adds any new topics
        new_topics = context["topics_discussed"] - prev_topics

        if new_topics and len(prev_topics) > 0:
            new_topic = list(new_topics)[0]
            return f"I see we're now talking about {new_topic}. That's an interesting switch from our previous topics!"

        # Check for Python questions with contextual awareness
        if "python" in user_input and context["topics_discussed"]:
            if "weather" in context["topics_discussed"]:
                return "Python can be used for weather data analysis and forecasting! Libraries like MetPy are specifically designed for meteorological calculations."
            elif "music" in context["topics_discussed"]:
                return "Python has libraries like librosa for music analysis and pygame for playing sounds. You can even create music with Python!"

        # Question counter responses
        if "?" in user_input:
            if context["question_count"] == 1:
                return "That's a good first question! I'm here to help with more."
            elif context["question_count"] == 5:
                context["mood"] = "tired"
                return "You ask a lot of questions! That's good for learning, but I'm getting a bit tired."
            elif context["question_count"] > 8:
                return "Wow, you're very curious today! So many questions!"

        # If no contextual response matched, fall back to basic responses
        if "python" in user_input:
            return "Python is a powerful programming language. Is there something specific about Python you'd like to know?"
        elif "weather" in user_input:
            return "Weather is always an interesting topic. Are you experiencing good weather today?"
        elif "bye" in user_input or "goodbye" in user_input:
            topics = len(context["topics_discussed"])
            questions = context["question_count"]
            return f"Goodbye, {context['user_name']}! We discussed {topics} topics and you asked {questions} questions. Come back soon!"
        else:
            return "I'm listening. Feel free to ask about Python, share your thoughts, or discuss other topics like weather or music."

    # Welcome and get user's name
    print(f"\nHello! I'm {bot_name}, a context-aware chatbot.")
    context["user_name"] = input("What's your name? ").strip()
    context["mood"] = "happy"  # Start in a happy mood

    print(f"\n{bot_name}> Nice to meet you, {context['user_name']}! Let's chat about Python, weather, music, or anything else on your mind. Type 'bye' to end our conversation.")

    # Main conversation loop
    while True:
        user_input = input(f"\n{context['user_name']}> ").strip()

        if user_input.lower() == "bye":
            print(f"\n{bot_name}> {get_contextual_response(user_input)}")
            break

        response = get_contextual_response(user_input)
        print(f"\n{bot_name}> {response}")

# Run the context-aware chatbot
# context_aware_chatbot()  # Uncomment to run
