number = int(input("Enter the Number: "))
len_digits = len(str(number))
temp_number = number
ans = 0
for i in range(0, len_digits):
    ans += (temp_number % 10) ** len_digits
    temp_number //= 10

if ans == number:
    print("It is an Armstrong Number.")
else:
    print("It is not an Armstrong Number.")