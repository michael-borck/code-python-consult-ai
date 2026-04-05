# Chatbot Project Milestones

Each chapter's Building Session adds one feature to the chatbot.
The chatbot starts as a 10-line terminal script and evolves into
a full-featured conversational program.

## Chapter Milestones

| Ch | Chapter | Chatbot Gains | Key Concept Shown |
|----|---------|--------------|-------------------|
| 1 | After Vibe Coding | Basic loop: greet, read input, echo, quit | The skeleton |
| 2 | Getting Started | Runs in Jupyter + script, proper comments | Execution environments |
| 3 | Values | Distinguishes between text and number responses | Data types matter |
| 4 | Variables | Remembers user name, tracks message count, constants | State via variables |
| 5 | Output | Formatted welcome screen, aligned output | f-strings, formatting |
| 6 | Input | Validates input, handles empty/unexpected answers | input() + validation |
| 7 | Operators | Responds differently based on message length, word count | Comparisons, logic |
| 8 | Using Functions | Uses len(), .lower(), .strip() on user input | Built-in functions |
| 9 | Creating Functions | Code split into get_response(), display_help(), main() | Function design |
| 10 | Making Decisions | Different responses for greetings, questions, farewells | if/elif/else |
| 11 | Lists | Stores conversation history, picks random responses | List operations |
| 12 | Loops | Processes each word in input, counts keywords | for/while patterns |
| 13 | Strings | Pattern matching on input, formats response text | String methods |
| 14 | Dictionaries | Maps keywords to response categories | Key-value lookup |
| 15 | Files | Saves/loads conversation history to file | File I/O |
| 16 | Errors | Graceful handling of missing files, bad input | try/except |
| 17 | Debugging | Debug mode toggle, verbose logging | Print debugging |
| 18 | Testing | pytest tests for get_response() | Test functions |
| 19 | Modules | Split into chatbot package: main, responses, history | Package structure |
| 20 | Objects | Chatbot class with state, methods, inheritance | OOP refactor |

## Cumulative State

By chapter 10, the chatbot should be ~40-50 lines with:
- Input loop, name memory, message counter
- Formatted output, input validation
- Functions for response logic, help, main loop
- if/elif/else for different response types

By chapter 15, the chatbot should be ~80-100 lines with:
- List-based conversation history
- Dictionary-based response mapping
- String pattern matching
- File persistence

By chapter 20, the chatbot should be a proper package with:
- Multiple modules (main, responses, history, config)
- A Chatbot class
- Error handling throughout
- Test suite
- Debug mode
