lower = int(input("Enter the lower range: "))
higher = int(input("Enter the Higher range: "))

for num in range(lower, higher+1):
    len_digits = len(str(num))
    temp_number = num
    ans = 0
    for i in range(0, len_digits):
        ans += (temp_number % 10) ** len_digits
        temp_number //= 10

    if ans == num:
        print(f"{num} is an Armstrong Number.")