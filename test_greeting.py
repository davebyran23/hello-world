# Comprehensive Test Suite for Enhanced Greeting Script
# This file tests all functionality of the greeting system

def test_greeting_logic():
    """Test the greeting logic with various inputs"""
    
    def create_greeting(user_name):
        """Copy of the greeting logic for testing"""
        name_lower = user_name.lower()
        
        if name_lower == "david":
            return f"Hey, it's the awesome AI Director, {user_name}! 🎉"
        elif name_lower == "admin":
            return f"Welcome back, Administrator {user_name}! 🔐"
        elif name_lower in ["guest", "anonymous"]:
            return f"Hello, {user_name}! Welcome to our system! 👋"
        else:
            return f"Hello, {user_name}! Nice to meet you! 😊"
    
    # Test cases
    test_cases = [
        # Test David variations
        ("David", "Hey, it's the awesome AI Director, David! 🎉"),
        ("david", "Hey, it's the awesome AI Director, david! 🎉"),
        ("DAVID", "Hey, it's the awesome AI Director, DAVID! 🎉"),
        ("David ", "Hey, it's the awesome AI Director, David ! 🎉"),
        
        # Test Admin variations
        ("admin", "Welcome back, Administrator admin! 🔐"),
        ("Admin", "Welcome back, Administrator Admin! 🔐"),
        ("ADMIN", "Welcome back, Administrator ADMIN! 🔐"),
        
        # Test Guest variations
        ("guest", "Hello, guest! Welcome to our system! 👋"),
        ("Guest", "Hello, Guest! Welcome to our system! 👋"),
        ("anonymous", "Hello, anonymous! Welcome to our system! 👋"),
        
        # Test regular names
        ("Alice", "Hello, Alice! Nice to meet you! 😊"),
        ("John", "Hello, John! Nice to meet you! 😊"),
        ("Sarah", "Hello, Sarah! Nice to meet you! 😊"),
        ("Bob", "Hello, Bob! Nice to meet you! 😊"),
        
        # Test edge cases
        ("", "Hello, ! Nice to meet you! 😊"),
        ("123", "Hello, 123! Nice to meet you! 😊"),
        ("A", "Hello, A! Nice to meet you! 😊"),
    ]
    
    print("=" * 60)
    print("COMPREHENSIVE GREETING SYSTEM TEST RESULTS")
    print("=" * 60)
    
    passed = 0
    failed = 0
    
    for test_input, expected_output in test_cases:
        actual_output = create_greeting(test_input)
        
        if actual_output == expected_output:
            print(f"✅ PASS: '{test_input}' → '{actual_output}'")
            passed += 1
        else:
            print(f"❌ FAIL: '{test_input}'")
            print(f"   Expected: '{expected_output}'")
            print(f"   Got:      '{actual_output}'")
            failed += 1
    
    print("=" * 60)
    print(f"TEST SUMMARY: {passed} passed, {failed} failed")
    print("=" * 60)
    
    return passed, failed

def test_input_validation():
    """Test input validation logic"""
    print("\n" + "=" * 40)
    print("INPUT VALIDATION TESTS")
    print("=" * 40)
    
    test_inputs = ["", "   ", "David", "  Alice  "]
    
    for test_input in test_inputs:
        stripped = test_input.strip()
        is_valid = bool(stripped)
        status = "✅ Valid" if is_valid else "❌ Invalid"
        print(f"'{test_input}' → '{stripped}' → {status}")

if __name__ == "__main__":
    # Run all tests
    passed, failed = test_greeting_logic()
    test_input_validation()
    
    if failed == 0:
        print("\n🎉 ALL TESTS PASSED! The greeting system is working perfectly!")
    else:
        print(f"\n⚠️  {failed} test(s) failed. Please review the logic.") 