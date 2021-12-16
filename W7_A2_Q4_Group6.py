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

# The list containing the cartesian product of A(A * A)
product_a = []


# -------Code for to get user input for the values for the list R------
# Input list R
# Number of sub lists
# list_size = 2
# num_list = int(input("Please enter the number of sublist R you will input: "))
# list_r = [[int(input("Please enter a single number and press enter: ")) for _ in range(list_size)]
#           for _ in range(num_list)]

# -------Code to get user input for the values for list A--------
# user_input_A = input("Enter the values of A").split(",")
# new_list = [int(i) for i in user_input_A]

# Functions

# Checking if R is a set by checking if the list R has any duplicate values
list_r_set = []
def checking_duplicatesR():
    """Checking if the given list R contains any duplicates"""
    for elem in list_r:
        if list_r.count(elem) > 1:
            return "R is not a set"
        else:
            list_r_set.append(1)
            return "R is a set"


# Input the list A and performing the cartesian product
def cartesian_product_A(user_input_A):
    """Input the list A and perform the cartesian product of A"""
    for i in user_input_A:
        for j in user_input_A:
            product_a.append([i, j])
    return product_a


# checking if R is a subset of A x A
list_r_s = []
def r_subset_cartesian_productA(product_a, list_r):
    for item in list_r:
        if item[0] in product_a and item[1] in product_a:
            list_r_s.append(1)
            return 'R is a subset of A'
        else:
            return 'R is not a subset of A'



# showing that R is not a relation on A
def checking_R_relation_A():
    if list_r_s == [1] and list_r_set == [1]:
        print("R is a relation on A")
    else:
        print("R is not a relation on A")


def reflexive(list_r, user_input_A):
    """Will return True if a relation R on the set A is reflexive, False otherwise."""
    values_not_reflexive = []
    for a in user_input_A:
        list_relation = [a, a]
        if list_relation not in list_r:
            values_not_reflexive.append(a)
    if len(values_not_reflexive) > 0:
        print("R is not reflexive", values_not_reflexive)
    else:
        print("R is reflexive")




# Checking for the property on symmetry on R
def symmetric(list_r_symmetry):
    values_not_symmetric = []
    for x in list_r_symmetry:
        for y in list_r_symmetry:
            if x[0] == y[1] and x[1] == y[0] and x not in list_true and y not in list_true:
                list_true.append(x)
                list_true.append(y)
                # print(list_true)
    if list_true == list_r_symmetry:
        print("R is symmetric")
    else:
        for x in list_r_symmetry:
            if x not in list_true:
                values_not_symmetric.append(x)
        print("R is not symmetric ", values_not_symmetric)


# Test Data for symmetry property of the R relation
list_r_symmetry = [[2, 3], [4, 4], [5, 5], [5, 2], [2, 4]]
list_true = []



# # Checks of R is symmetric
def transitive(list_r):
    list_present = []
    for x in list_r:
        for y in list_r:
            for z in list_r:
                if x[1] == y[0] and y[1] == z[1] and x[0] == z[0] and x not in list_r and y not in list_r:
                    pass
                elif x[1] == y[0] and y[1] != z[1] and x[0] != z[0]:
                    list_present.append(z)
    if list_present == []:
        print("R is transitive")
    else:
        print("R is not transitive", list_present)


# Trial Data
list_r = [[2, 3], [4, 4], [5, 5], [5, 2], [2, 4]]
user_input_A = [1, 2, 3, 4]
# # Calls the functions
print(checking_duplicatesR())
cartesian_product_A(user_input_A)
print(r_subset_cartesian_productA(product_a, list_r))
checking_R_relation_A()
reflexive(list_r, user_input_A)
transitive(list_r)
symmetric(list_r_symmetry)

