def calculate_statistics(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count if count > 0 else 0
    return total, count, average

data = [10, 20, 30, 40, 50]
total, count, average = calculate_statistics(data)

print(f"Total: {total}")
print(f"Count: {count}")
print(f"Average: {average}")
