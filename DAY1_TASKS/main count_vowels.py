from count_vowels import vowel_count

def main():
    print("=== Vowel Counter Program ===")
    user_text = input("Enter Your Text: ")
    count = vowel_count(user_text)
    print("\nResult:")
    print(f"Text: '{user_text}'")
    print(f"Number of vowels: {count}")

if __name__ == "__main__":
    main()