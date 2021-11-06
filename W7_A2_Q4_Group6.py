# Question 4
# Write a programme that takes as input a finite set or list (you may decide) A and a list R where
# R is of the form (written mathematically):
# R = {(x1, y1),(x2, y2), ...,(xn, yn)}.
# Your code should first check if R is a relation on A (that is, if R is a set and if R ⊆ A × A).
# If R is not a relation on A, your programme should output a statement to this effect.
# If R is a relation on A then your programme should output which of the following properties
# the relation satisfies:
# a) reflexive,
# b) transitive, and/or
# c) symmetric.


# Input list R
# Number of sub lists

# The list containing the cartesian product of A
product_a = []

# Input list R
# Number of sub lists
list_size = 2
num_list = int(input("Please enter the number of sublist R you will input: "))
list_r = [[int(input("Please enter a single number and press enter: ")) for _ in range(list_size)]
          for _ in range(num_list)]
print(list_r)


# Checking if R is a set by checking if the list R has any duplicate values
def checking_duplicatesR():
    """Checking if the given list R contains any duplicates"""
    for elem in list_r:
        if list_r.count(elem) > 1:
            print("R is not a set")
        else:
            print("R is a set")


checking_duplicatesR()


# Input the list A and performing the cartesian product
def cartesian_product_A():
    """Input the list A and perform the cartesian product of A"""
    user_input_A = input("Enter the values of A").split(",")
    new_list = [int(i) for i in user_input_A]
    for i in new_list:
        for j in new_list:
            product_a.append([i, j])
    return product_a


print(cartesian_product_A())


# checking if R is a subset of A x A
def r_subset_cartesian_productA(product_a, list_r):
    """Checking if R is a subset of the cartesian product of A"""
    # The condition to check whether the list R is a subset of cartesian product of A
    for item in list_r:
        if item not in product_a:
            print("R is not a subset of A")
        else:
            print("R is a subset of A")


(r_subset_cartesian_productA(product_a, list_r))
# showing that R is not a relation on A
# if list_r == "R is a set":
#     if list_r == "R is a subset of A":
#         print("R is a relation on A")
# else:
#     print("R is not a relation on A")
# possible_set_r = set([i for j in list_r for i in j])
