def capitalize_first_character(s):
    if s:
        return s[0].upper() + s[1:]
    return s


input_string = str(input("Enter a string: "))
capitalized_string = capitalize_first_character(input_string)

print(f"Original string: '{input_string}'")
print(f"Capitalized string: '{capitalized_string}'")
