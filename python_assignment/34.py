def decimal_to_binary(n):
    # Base case: if the number is 0 or 1, return the string representation of the number
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    # Recursive case: divide the number by 2 and prepend the remainder
    else:
        return decimal_to_binary(n // 2) + str(n % 2)


decimal_number = int(input("Enter the Number: "))
binary_representation = decimal_to_binary(decimal_number)
print(f"Decimal {decimal_number} is Binary {binary_representation}")
