num = int(input("Enter a number: "))

is_prime = True
for i in range(0,num):
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            is_prime = False

    if is_prime:
        print(f"{i}\n")
