def summation(num):
    if num > 0:
        return num+summation(num - 1)
    return 0


n = int(input("Enter a Number: "))
ans = summation(n)
print(ans)
