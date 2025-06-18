# This script asks the user for their name and then prints a personalized greeting.
# Enhanced with conditional logic for special welcome messages.

# 1. Ask the user a question: "What is your name?"
#    Whatever they type in, we'll store it in a variable called 'user_name'.
user_name = input("What is your name? ")

# 2. Create a personalized greeting message using conditional logic.
#    If the user's name is "David", print a special welcome message.
#    For any other name, print the regular greeting.
if user_name.lower() == "david":
    # Special welcome message for David
    greeting_message = f"Hey, it's the awesome AI Director, {user_name}!"
else:
    # Regular greeting for everyone else
    greeting_message = "Hello, " + user_name + "!"

# 3. Print the complete personalized greeting to the screen.
print(greeting_message) 