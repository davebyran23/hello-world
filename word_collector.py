def get_user_words():
    """
    Asks the user for a noun, verb, and adjective and returns them as a tuple.
    
    Returns:
        tuple: A tuple containing (noun, verb, adjective) as strings
    """
    print("Let's collect some words for your story!")
    print("-" * 40)
    
    # Get noun from user
    noun = input("Please enter a noun (person, place, or thing): ").strip()
    while not noun:
        print("Please enter a valid noun!")
        noun = input("Please enter a noun (person, place, or thing): ").strip()
    
    # Get verb from user
    verb = input("Please enter a verb (action word): ").strip()
    while not verb:
        print("Please enter a valid verb!")
        verb = input("Please enter a verb (action word): ").strip()
    
    # Get adjective from user
    adjective = input("Please enter an adjective (describing word): ").strip()
    while not adjective:
        print("Please enter a valid adjective!")
        adjective = input("Please enter an adjective (describing word): ").strip()
    
    print("-" * 40)
    print(f"Great! You provided: {noun}, {verb}, {adjective}")
    
    return noun, verb, adjective

# Example usage
if __name__ == "__main__":
    noun, verb, adjective = get_user_words()
    print(f"\nYour words: Noun = {noun}, Verb = {verb}, Adjective = {adjective}") 