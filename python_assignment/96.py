def remove_duplicates(input_list):
    return list(set(input_list))

original_list = input("Enter a list: ").split(" ")
unique_list = remove_duplicates(original_list)

print("Original list:", original_list)
print("List after removing duplicates:", unique_list)
