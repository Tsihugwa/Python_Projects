import random

# list of possible responses
responses = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes - definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful.",
]

def ask_question():
    # prompt the user to ask a question
    print("Welcome to the Magic 8 Ball game!")
    print("Ask a yes or no question and the Magic 8 Ball will provide an answer.")
    question = input("What is your question? (Enter 'q' to quit)")
    if question.lower() == 'q':
        return
    print("Thinking...")
    
    # choose a random response
    response = random.choice(responses)
    print(response)

# main loop
while True:
    ask_question()
    # ask the user if they want to ask another question
    another = input("Would you like to ask another question? (y/n) ")
    if another.lower() == "n":
        break

