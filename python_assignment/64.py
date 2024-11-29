main_string = str(input("Enter the string: "))
start_index = int(input("Enter the start index: "))
end_index = int(input("Enter the End index: "))
substring = main_string[start_index:end_index]

print("Original String:", main_string)
print(f"Substring (from index {start_index} to {end_index}):", substring)
