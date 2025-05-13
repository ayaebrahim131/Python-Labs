def vowel_count(input_str):
    vowel_chars = "aeiouAEIOU"
    vowel_num = 0
    for char in input_str:
        if char.lower() in vowel_chars:
            vowel_num += 1
    return vowel_num

user_text = input("Enter Your Text: ")
print("Vowels count:", vowel_count(user_text))