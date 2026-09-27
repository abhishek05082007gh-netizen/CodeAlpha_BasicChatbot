"""
CodeAlpha Internship - Task 4: Basic Chatbot
Author: Abhishek Singh
Description: A simple rule-based conversational chatbot using functions, loops, and conditional statements.
"""

from datetime import datetime

def get_bot_response(user_input):
    """
    Processes user input and returns a predefined response based on rule matching.
    """
    cleaned_input = user_input.strip().lower()

    # Greetings
    if any(greet in cleaned_input for greet in ["hello", "hi", "hey", "greetings"]):
        return "Hi there! How can I help you today?"

    # Well-being queries
    elif any(q in cleaned_input for q in ["how are you", "how are you doing", "how are things"]):
        return "I'm doing great, thank you for asking! How are you?"

    # Identity queries
    elif any(name in cleaned_input for name in ["who are you", "what is your name", "what are you"]):
        return "I am AlphaBot, a rule-based Python chatbot created for the CodeAlpha Internship!"

    # Help commands
    elif "help" in cleaned_input:
        return ("You can talk to me by saying hello, asking how I am, asking for the time or date, "
                "asking for a joke, or saying goodbye to exit.")

    # Time & Date queries
    elif "time" in cleaned_input:
        current_time = datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}."

    elif "date" in cleaned_input or "today" in cleaned_input:
        current_date = datetime.now().strftime("%A, %B %d, %Y")
        return f"Today's date is {current_date}."

    # Casual talk & jokes
    elif "joke" in cleaned_input:
        return "Why do programmers prefer dark mode? Because light attracts bugs! 🐛"

    elif "thank" in cleaned_input:
        return "You're very welcome! Feel free to ask anything else."

    # Exit queries
    elif any(bye in cleaned_input for bye in ["bye", "goodbye", "exit", "quit", "see you"]):
        return "Goodbye! Have a wonderful day!"

    # Default fallback response
    else:
        return "I'm sorry, I don't quite understand that. Type 'help' to see what I can do!"

def main():
    print("=" * 55)
    print("       WELCOME TO ALPHABOT (BASIC PYTHON CHATBOT)    ")
    print("=" * 55)
    print("Type your message below. Type 'bye' or 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip()

        # Handle empty input
        if not user_input:
            continue

        response = get_bot_response(user_input)
        print(f"AlphaBot: {response}\n")

        # Exit condition check
        if any(bye in user_input.lower() for bye in ["bye", "goodbye", "exit", "quit"]):
            break

if __name__ == "__main__":
    main()
