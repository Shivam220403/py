dictionary = {
    "apple":"red",
    "banana":"yellow",
    "orange":"orange"
}
fruit = str(input("Enter a fruit to search: ")).lower()

if fruit in dictionary:
    print("This fruit is in the dictionary")
else:
    print("This fruit is not in the dictionary")
