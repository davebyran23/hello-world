# This script asks the user for their name and then prints a personalized greeting.

# 1. Ask the user a question: "What is your name?"
#    Whatever they type in, we'll store it in a variable called 'user_name'.
user_name = input("What is your name? ")

# 2. Create a personalized greeting message.
#    We combine the fixed text "Hello, " with the user's name from the 'user_name' variable,
#    and then add an exclamation mark "!".
greeting_message = "Hello, " + user_name + "!"

# 3. Print the complete personalized greeting to the screen.
print(greeting_message) 