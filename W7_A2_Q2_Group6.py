# Question 2
# Getting user input
a = [int(item) for item in input("Enter the values for A").split()]
b = [int(item) for item in input("Enter the values for B").split()]

# converting user input list a and b to sets
values_a = set(a)
values_b = set(b)

# checking A - B
possible_set_difference = values_a.difference(values_b)
print(possible_set_difference)

# checking  B ⊆ A
possible_b_subseta = values_b.issubset(values_a)
print(possible_b_subseta)

# checking A x B
cartesian_product = [(i, j) for i in a for j in b]
cartesian_product_set = set(cartesian_product)
print(cartesian_product_set)