s = str(input("Input String: "))
vowel_count = {
    'a':0,
    'e':0,
    'i':0,
    'o':0,
    'u':0
}
for char in s:
    if char == 'a':
        vowel_count['a'] += 1
    elif char == "e":
        vowel_count['e'] += 1
    elif char == "i":
        vowel_count['i'] += 1
    elif char == "o":
        vowel_count['o'] += 1
    elif char == "u":
        vowel_count['u'] += 1

print(f"Number of Vowels: ")
for i in vowel_count:
    print(f"{i}: {vowel_count[i]}")

