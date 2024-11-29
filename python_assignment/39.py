 import string

s = str(input("Input a string: "))
s = list(s)
punctuation = string.punctuation
no_punctuation_string = ''.join([char for char in s if char not in punctuation])
print(no_punctuation_string)