my_dict = {
    'name': 'Shivam',
    'age': 21,
    'city': 'Dehradun'
}
print("Before deletion: ")
print(my_dict)
element_to_delete = input("Enter the element to delete: ")
del my_dict[element_to_delete]
print("After deletion: ")
print(my_dict)