"""
Strings - Mastering Text Manipulation

Extracted from the companion book.
"""

def parse_command(message):
    """
    Parse a user command message to extract structured information.

    Args:
        message (str): The user message to parse

    Returns:
        dict: A dictionary containing the extracted information:
            - action: The identified action type
            - person: The person's name (or None if not found)
            - time: The time specification (or None if not found)
            - date: The date reference (or None if not found)
    """
    # Initialize result dictionary with default values
    result = {
        'action': None,
        'person': None,
        'time': None,
        'date': None
    }

    # Convert to lowercase for easier parsing
    message = message.lower().strip()

    # Identify the action type
    action_keywords = {
        'remind': 'reminder',
        'call': 'call',
        'text': 'message',
        'message': 'message',
        'set meeting': 'meeting',
        'schedule': 'meeting',
        'appointment': 'appointment'
    }

    for keyword, action_type in action_keywords.items():
        if keyword in message:
            result['action'] = action_type
            break

    # Extract time information
    time_indicators = ['at', 'on']
    words = message.split()

    for i, word in enumerate(words):
        # Look for time indicators followed by time
        if word in time_indicators and i < len(words) - 1:
            next_word = words[i + 1]

            # Check for time patterns like "3pm", "10am", "15:30"
            if ('am' in next_word or 'pm' in next_word or ':' in next_word):
                result['time'] = next_word

                # Look for date reference after the time
                if i + 2 < len(words):
                    date_keywords = ['tomorrow', 'today', 'monday', 'tuesday', 'wednesday',
                                    'thursday', 'friday', 'saturday', 'sunday']
                    if words[i + 2] in date_keywords:
                        result['date'] = words[i + 2]

            # If the next word is a date reference, look for time after it
            elif next_word in ['tomorrow', 'today', 'monday', 'tuesday', 'wednesday',
                              'thursday', 'friday', 'saturday', 'sunday']:
                result['date'] = next_word

                # Check if there's a time after the date
                if i + 3 < len(words) and words[i + 2] == 'at':
                    potential_time = words[i + 3]
                    if ('am' in potential_time or 'pm' in potential_time or ':' in potential_time):
                        result['time'] = potential_time

    # Extract person name using common patterns
    person_indicators = ['with', 'to call', 'to text', 'to message']

    for indicator in person_indicators:
        if indicator in message:
            # Find the position of the indicator
            pos = message.find(indicator) + len(indicator)

            # Extract the text after the indicator
            remaining = message[pos:].strip()

            # Look for the end of the name (until the next keyword or punctuation)
            end_markers = ['at', 'on', 'tomorrow', 'today', ',', '.']
            end_pos = len(remaining)

            for marker in end_markers:
                marker_pos = remaining.find(marker)
                if marker_pos != -1 and marker_pos < end_pos:
                    end_pos = marker_pos

            # Extract and clean the person name
            name = remaining[:end_pos].strip()

            # Only set if it looks like a name (not empty, not just a single character)
            if name and len(name) > 1:
                # Capitalize the name properly
                result['person'] = ' '.join(word.capitalize() for word in name.split())

            break

    # Alternative person extraction if previous method didn't work
    if result['person'] is None and 'remind me to call' in message:
        pos = message.find('remind me to call') + len('remind me to call')
        remaining = message[pos:].strip()

        # Find the end of the name
        end_markers = ['at', 'on', 'tomorrow', 'today', ',', '.']
        end_pos = len(remaining)

        for marker in end_markers:
            marker_pos = remaining.find(marker)
            if marker_pos != -1 and marker_pos < end_pos:
                end_pos = marker_pos

        name = remaining[:end_pos].strip()
        if name and len(name) > 1:
            result['person'] = ' '.join(word.capitalize() for word in name.split())

    return result

# Testing the function
examples = [
    "remind me to call John at 3pm tomorrow",
    "set meeting with Sarah on Tuesday at 10am",
    "schedule appointment with Dr. Smith on Friday at 2:30pm",
    "text Alex tomorrow at 9am",
    "remind me to take medicine at 8pm"
]

for example in examples:
    result = parse_command(example)
    print(f"\nInput: {example}")
    print(f"Parsed: {result}")
