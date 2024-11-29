def count_character_occurrences(s, char):
    return s.count(char)


input_string = str(input("Enter a string: "))
character_to_count = str(input("Enter the character you want to check: "))
occurrences = count_character_occurrences(input_string, character_to_count)

print(f"The character '{character_to_count}' occurs {occurrences} times in the string.")
