def i_location(user_text):
    i_positions = []  

    for position, character in enumerate(user_text):
        if character.lower() == 'i':
            i_positions.append(position)
    
    return i_positions

text_input = input("Welcome, Enter your text: ")
result = i_location(text_input)

print(f"The letter 'i' appears at positions: {result}")