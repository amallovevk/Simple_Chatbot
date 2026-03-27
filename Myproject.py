# -------------------------------------------
# Simple Keyword-Based Chatbot in Python
# -------------------------------------------

print("🤖 ChatBot: Hello! I am your simple chatbot. Type 'bye' to exit.\n")

# Predefined keyword-response dictionary
responses = {
    "hello": "Hello! How can I help you today?",
    "hi": "Hi there! What can I do for you?",
    "hey": "Hey! How's your day going?",
    "time": "I don't have a watch, but I know it's always a good time to learn Python!",
    "name": "I'm ChatPy, your friendly Python chatbot!",
    "help": "Sure! Tell me what you need help with.",
    "python": "Python is a powerful and beginner-friendly programming language!",
    "robotics": "Robotics combines programming, electronics, and mechanics—exciting field!",
    "ktu": "KTU students are awesome! How can I assist you with your academics?",
    "project": "I can help you with project ideas, code, or documentation. Just ask!"
}

# Function to find a matching response
def get_response(user_input):
    user_input = user_input.lower()

    # Check if any keyword is present in user input
    for keyword in responses:
        if keyword in user_input:
            return responses[keyword]

    # Default fallback response
    return "I'm not sure I understand. Can you rephrase that?"

# Chat loop
while True:
    user_text = input("You: ")

    if user_text.lower() == "bye":
        print("🤖 ChatBot: Goodbye! Have a great day! 👋")
        break

    reply = get_response(user_text)
    print("🤖 ChatBot:", reply)
