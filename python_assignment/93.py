import itertools


def compute_permutations(s):
    permutations = [''.join(p) for p in itertools.permutations(s)]
    return permutations


input_string = str(input("Enter a string: "))
permuted_strings = compute_permutations(input_string)

print("All permutations of the string are:")
for perm in permuted_strings:
    print(perm)
