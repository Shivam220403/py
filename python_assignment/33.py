def factorial(num):
    if num > 1:
        return num*factorial(num-1)
    return 1


n = int(input("Enter a Number: "))
ans = factorial(n)
print(ans)