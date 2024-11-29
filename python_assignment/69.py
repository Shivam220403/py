arr = []
arr = input("Enter a list: ").split(" ")
item = input("Enter the item: ")
count = 0
for i in arr:
    if item == i:
        count += 1
print(f"{item} has occurred {count} times in {arr}")
