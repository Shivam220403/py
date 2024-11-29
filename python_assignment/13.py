num = int(input("Enter a number: "))

if num <= 1:
    print(f"{num} is neither Prime nor Composite.")
else:
    is_prime = True  # Assume number is prime
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{num} is a Prime Number.")
    else:
        print(f"{num} is a Composite Number.")
