def parse_string(input_str):
    try:
        result = int(input_str)
        print(f"Parsed as integer: {result}")
    except ValueError:
        try:
            result = float(input_str)
            print(f"Parsed as float: {result}")
        except ValueError:
            print(f"Cannot parse '{input_str}' as a float or int")


input_str = str(input("Enter a string: "))
parse_string(input_str)
