def reverse_string(text):
    """Simple function to reverse a string"""
    return text[::-1]

def main():
    print("=== Simple String Reverser ===")
    print("Enter a string to reverse (or 'quit' to exit):")
    
    while True:
        user_input = input("\nEnter string: ").strip()
        
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        
        if user_input:
            reversed_text = reverse_string(user_input)
            print(f"Original: {user_input}")
            print(f"Reversed: {reversed_text}")
        else:
            print("Please enter a valid string.")

if __name__ == "__main__":
    main() 