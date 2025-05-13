from find_i import i_location
def main():
    print("=== i Locator Program ===")
    print("This program finds all positions of letter 'i' in your text")
    text_input = input("Please enter your text: ")
    
    positions = i_location(text_input)
    
    print("\nResults:")
    if positions:
        print(f"Found 'i' at positions: {positions}")
        print(f"Total occurrences: {len(positions)}")
    else:
        print("No letter 'i' found in the text")

if __name__ == "__main__":
    main()