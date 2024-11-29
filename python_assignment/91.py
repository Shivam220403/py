str1 = str(input("Enter a string :"))
str2 = str(input("Enter another string: "))

cpy_str1 = list(str1)
cpy_str2 = list(str2)

cpy_str1.sort()
cpy_str2.sort()
if cpy_str2 == cpy_str1:
    print("The Strings are anagram")
else:
    print("The Strings are not anagram")