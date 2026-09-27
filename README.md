# CodeAlpha_BasicChatbot

A rule-based **Basic Chatbot** built in Python as part of the **CodeAlpha Python Programming Internship**.

## 📌 Task Overview (Task 4)
- **Goal:** Build a simple rule-based chatbot capable of interacting with users through predefined inputs and responses.
- **Scope & Features:**
  - Understands greetings (`hello`, `hi`, `hey`).
  - Responds to well-being questions (`how are you`).
  - Provides date, time, and bot identity details.
  - Shares programming humor/jokes.
  - Exits gracefully on farewell inputs (`bye`, `goodbye`, `exit`).
  - Fallback mechanism for unrecognized inputs with a `help` guide.

## 🛠️ Key Concepts Used
- Functions (`def`) and modular structure
- `if-elif-else` conditional rule matching
- `while` loops for continuous interactive chat
- String handling & case normalization (`.lower()`, `.strip()`)
- `datetime` module for real-time information

## 🚀 How to Run
1. Make sure Python 3 is installed.
2. Clone the repository:
   ```bash
   git clone https://github.com/abhishek05082007gh-netizen/CodeAlpha_BasicChatbot.git
   ```
3. Navigate into the directory:
   ```bash
   cd CodeAlpha_BasicChatbot
   ```
4. Run the chatbot:
   ```bash
   python chatbot.py
   ```

## 💬 Sample Conversation
```text
=======================================================
       WELCOME TO ALPHABOT (BASIC PYTHON CHATBOT)    
=======================================================
Type your message below. Type 'bye' or 'exit' to quit.

You: hello
AlphaBot: Hi there! How can I help you today?

You: how are you
AlphaBot: I'm doing great, thank you for asking! How are you?

You: tell me a joke
AlphaBot: Why do programmers prefer dark mode? Because light attracts bugs! 🐛

You: bye
AlphaBot: Goodbye! Have a wonderful day!
```
