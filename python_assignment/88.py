def reverse_number(num):
    reversed_num = int(str(num)[::-1])
    return reversed_num


number = int(input("Enter a number: "))
reversed_number = reverse_number(number)

print(f"The reversed number is: {reversed_number}")
