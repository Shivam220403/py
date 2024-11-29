# Define two sets
set_A = {1, 2, 3, 4, 5}
set_B = {4, 5, 6, 7, 8}

print("Set A:", set_A)
print("Set B:", set_B)

# Union of sets
union_set = set_A.union(set_B)
print("\nUnion of A and B:", union_set)

# Intersection of sets
intersection_set = set_A.intersection(set_B)
print("Intersection of A and B:", intersection_set)

# Difference of sets (A - B)
difference_set = set_A.difference(set_B)
print("Difference of A and B (A - B):", difference_set)

# Symmetric Difference of sets (A Δ B)
symmetric_difference_set = set_A.symmetric_difference(set_B)
print("Symmetric Difference of A and B:", symmetric_difference_set)

# Check if A is a subset of B
is_subset = set_A.issubset(set_B)
print("\nIs A a subset of B?:", is_subset)

# Check if A is a superset of B
is_superset = set_A.issuperset(set_B)
print("Is A a superset of B?:", is_superset)

# Check if A and B are disjoint sets (no common elements)
are_disjoint = set_A.isdisjoint(set_B)
print("Are A and B disjoint?:", are_disjoint)
