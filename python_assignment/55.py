try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except (ValueError, ZeroDivisionError) as e:
    print("An error occurred:", e)
