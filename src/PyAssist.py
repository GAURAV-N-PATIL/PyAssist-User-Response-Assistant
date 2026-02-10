# main function
# This is the main function that will run the program. It will take user input and process it accordingly.

# Define keywords for intent recognition
Greeting_keywords = ["hello", "hi", "hey", "greetings","hey there","good morning","good afternoon","good evening","how are you","what's up","how's it going","hello there","hi PyAssist"]
Exit_keywords = ["exit", "quit", "goodbye", "bye","see you later","take care","farewell","catch you later","talk to you later","have a nice day","have a good day"]
Identity_keywords = ["who are you", "what is your name", "what do you do", "what can you do","tell me about yourself","what's your name","what's your purpose","what's your function","what's your role"]
intent = "Unknown"

# Output the recognized intent
def output_response(intent):
    if intent == "Greeting":
        print("Hello! How can I assist you today?")
    elif intent == "Exit":
        print("Goodbye! Have a great day!")
        exit()
    elif intent == "Identity":
        print("I am PyAssist, your personal assistant designed to help you with various tasks.")
    else:
        print("I'm sorry, I didn't understand that command.")

# Respond to the user based on the recognized intent
while intent not in Exit_keywords:
    # Normalize the user input by stripping whitespace and converting it to lowercase
    User_input = input("Enter a command: ")
    User_input = User_input.strip()
    User_input = User_input.lower()
    # intent recognition based on the user input
    if User_input in Greeting_keywords:
        intent = "Greeting"
    elif User_input in Exit_keywords:
        intent = "Exit"
    elif User_input in Identity_keywords:
        intent = "Identity"
    output_response(intent)

# function to run the main program
def main():
    print("Welcome to PyAssist!")
if __name__ == "__main__":
    main()