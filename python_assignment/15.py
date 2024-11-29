def factorial(num):
    if num > 0:
        return num*factorial(num-1)
    return 1


n = int(input("Input the Number: "))
print(f"The factorial of {n} is {factorial(n)}")
