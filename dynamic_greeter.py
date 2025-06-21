# Dynamic Greeter - Interactive and Personalized Greeting Program
# This program adapts to each user and the moment they run it

import datetime
import random

def get_current_time_info():
    """Get current time and date information"""
    now = datetime.datetime.now()
    hour = now.hour
    day_name = now.strftime("%A")
    month_name = now.strftime("%B")
    day_number = now.day
    
    return hour, day_name, month_name, day_number

def get_time_greeting(hour):
    """Return appropriate greeting based on time of day"""
    if 5 <= hour < 12:
        return "Good morning"
    elif 12 <= hour < 17:
        return "Good afternoon"
    elif 17 <= hour < 21:
        return "Good evening"
    else:
        return "Good night"

def get_special_greeting(name):
    """Return special greetings for specific names"""
    name_lower = name.lower()
    
    special_greetings = {
        "david": "Hey there, AI Director! 🎉",
        "admin": "Welcome back, Administrator! 🔐",
        "guest": "Hello, welcome to our system! 👋",
        "alice": "Wonderful to see you, Alice! ✨",
        "bob": "Hey Bob, great to have you here! 🚀"
    }
    
    return special_greetings.get(name_lower, None)

def get_day_enthusiasm(day_name):
    """Add day-specific enthusiasm to the greeting"""
    day_enthusiasm = {
        "Monday": "Let's start the week strong! 💪",
        "Tuesday": "Tuesday energy is flowing! ⚡",
        "Wednesday": "Hump day - we're halfway there! 🐪",
        "Thursday": "Almost Friday - keep going! 🎯",
        "Friday": "TGIF! Weekend is almost here! 🎉",
        "Saturday": "Perfect day for relaxation! 😌",
        "Sunday": "Sunday vibes - recharge time! 🌅"
    }
    
    return day_enthusiasm.get(day_name, "Have a wonderful day! 🌟")

def create_dynamic_greeting(name, hour, day_name, month_name, day_number):
    """Create a personalized, dynamic greeting"""
    
    # Get base time greeting
    time_greeting = get_time_greeting(hour)
    
    # Check for special name greeting
    special_greeting = get_special_greeting(name)
    
    if special_greeting:
        # Use special greeting for recognized names
        greeting = f"{special_greeting}"
    else:
        # Create personalized greeting for others
        greeting = f"{time_greeting}, {name}!"
    
    # Add day-specific enthusiasm
    day_message = get_day_enthusiasm(day_name)
    
    # Add date information
    date_info = f"Today is {day_name}, {month_name} {day_number}"
    
    return greeting, day_message, date_info

def get_user_name():
    """Get and validate user name input"""
    while True:
        name = input("What's your name? ").strip()
        if name:
            return name
        else:
            print("Please enter a valid name.")

def main():
    """Main function to run the Dynamic Greeter"""
    print("=" * 60)
    print("🌟 WELCOME TO THE DYNAMIC GREETER 🌟")
    print("=" * 60)
    
    try:
        # Get user input
        user_name = get_user_name()
        
        # Get current time information
        hour, day_name, month_name, day_number = get_current_time_info()
        
        # Create dynamic greeting
        greeting, day_message, date_info = create_dynamic_greeting(
            user_name, hour, day_name, month_name, day_number
        )
        
        # Display the complete greeting
        print("\n" + "=" * 40)
        print(greeting)
        print(day_message)
        print(date_info)
        print("=" * 40)
        
        # Additional personalized information
        print(f"\n📊 Quick Stats:")
        print(f"   • Name length: {len(user_name)} characters")
        print(f"   • Current time: {datetime.datetime.now().strftime('%I:%M %p')}")
        print(f"   • Time of day: {get_time_greeting(hour).lower()}")
        
        print(f"\n✨ Thank you for using the Dynamic Greeter! ✨")
        
    except KeyboardInterrupt:
        print("\n\n👋 Greeting interrupted. Goodbye!")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")

if __name__ == "__main__":
    main() 