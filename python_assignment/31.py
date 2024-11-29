def fibonacci(num):
    if num > 1:
        return fibonacci(num-1) + fibonacci(num-2)
    return 1


n = int(input("Enter the number of digits: "))
for i in range(0, n):
    ans = fibonacci(i)
    print(ans)
