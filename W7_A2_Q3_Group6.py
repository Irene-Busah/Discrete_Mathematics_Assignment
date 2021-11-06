# Write a programme that takes as input 2 finite lists of any size, A, B, and outputs the following:
# a) the truth value of B ⊆ A,
# b) a list representing the set A − B,
# c) a list representing the set A × B.
# This is the same question as Question 2 except you are not allowed to use the set environment in
# Python nor are you allowed to use in-built or package Python functions specific to sets which output
# the required sets immediately. You must use lists, for loops, if statements, and other basic Python
# commands.

# The function accepts two lists from the user
def finite_list(list_A, list_B):
    new_list_A = list(list_A)  # converts the first input of the user into list
    new_list_B = list(list_B)

    # The condition to check whether the list_B is a subset of list_A
    for item in new_list_B:
        if item not in new_list_A:
            return "False, B is not a subset of A"
        # if len(new_list_A) > len(new_list_B):
        #     return False
        # else:
    return "True, B is a subset of A"


def list_difference(list_A, list_B):
    new_list_A = list(list_A)               # converts the first input of the user into list
    new_list_B = list(list_B)

    list_diff = [val for val in new_list_A + new_list_B if val not in new_list_B]
    return list_diff


def cartesian_product(list_A, list_B):
    cartesian_pro = [[a, b] for a in list_A for b in list_B]
    return cartesian_pro


# accepts input from the user

list_1 = ["Irene", "Myra", "Nelson", "Micheal"]
list_2 = ["Irene", "Micheal", "Mike"]

# calls the respective functions for each
results = finite_list(list_1, list_2)
print(results)
print("")
answers = list_difference(list_1, list_2)
print(answers)
print("")
result = cartesian_product(list_1, list_2)
print(result)
print("")

list_one = ["Irene", "Myra", "Nelson", "Micheal"]
list_two = ["Irene", "Micheal"]

# calls the respective functions for each
results = finite_list(list_one, list_two)
print(results)
print("")
answers = list_difference(list_one, list_two)
print(answers)
print("")
result = cartesian_product(list_one, list_two)
print(result)

