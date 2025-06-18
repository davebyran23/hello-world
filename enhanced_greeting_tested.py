# Enhanced Greeting Script - Thoroughly Tested Version
# This script asks the user for their name and prints personalized greetings with conditional logic.

def get_user_name():
    """Get user name with input validation"""
    while True:
        user_name = input("What is your name? ").strip()
        if user_name:  # Check if name is not empty
            return user_name
        else:
            print("Please enter a valid name.")

def create_greeting(user_name):
    """Create personalized greeting based on user name"""
    # Convert to lowercase for case-insensitive comparison
    name_lower = user_name.lower()
    
    # Conditional logic for different greetings
    if name_lower == "david":
        return f"Hey, it's the awesome AI Director, {user_name}! 🎉"
    elif name_lower == "admin":
        return f"Welcome back, Administrator {user_name}! 🔐"
    elif name_lower in ["guest", "anonymous"]:
        return f"Hello, {user_name}! Welcome to our system! 👋"
    else:
        return f"Hello, {user_name}! Nice to meet you! 😊"

def main():
    """Main function to run the greeting program"""
    print("=" * 50)
    print("ENHANCED GREETING SYSTEM")
    print("=" * 50)
    
    try:
        # Get user name
        user_name = get_user_name()
        
        # Create and display greeting
        greeting = create_greeting(user_name)
        print("\n" + greeting)
        
        # Additional feedback
        print(f"\nName length: {len(user_name)} characters")
        print(f"Name in lowercase: {user_name.lower()}")
        print(f"Name in uppercase: {user_name.upper()}")
        
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user. Goodbye!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main() 