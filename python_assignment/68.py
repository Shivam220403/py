def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

input_str = input("Enter a string: ")

if is_float(input_str):
    print(f"'{input_str}' is a float.")
else:
    print(f"'{input_str}' is not a float.")
