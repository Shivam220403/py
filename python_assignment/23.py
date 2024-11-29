def decimaltobinary(n):
    answer = []
    if n == 0:
        answer.append('0')
    while n > 0:
        remainder = n % 2
        answer.insert(0, str(remainder))
        n //= 2
    print(''.join(answer))


def decimaltooctal(n):
    answer = []
    if n == 0:
        answer.append('0')
    while n > 0:
        remainder = n % 8
        answer.insert(0, str(remainder))
        n //= 8
    print(''.join(answer))


def decimaltohexadecimal(n):
    answer = []
    hex_digits = '0123456789ABCDEF'
    if n == 0:
        answer.append('0')
    while n > 0:
        remainder = n % 16
        answer.insert(0, hex_digits[remainder])
        n //= 16
    print(''.join(answer))


num = int(input("Input the Number: "))
choice = str(input("Choose between Binary, Octal, Hexadecimal: ")).lower()

if choice == "binary":
    decimaltobinary(num)
elif choice == "octal":
    decimaltooctal(num)
elif choice == "hexadecimal":
    decimaltohexadecimal(num)
else:
    print("Wrong choice")