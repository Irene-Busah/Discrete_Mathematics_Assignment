# ---------------------------- Question 2 --------------------------------

# Write a programme that takes as input 2 finite sets of any size, A, B, and outputs the following:
# a) the truth value of B ⊆ A,
# b) the set A − B,
# c) the set A × B.
# You may need to investigate the use of sets in Python. Please see the following website for a short
# introduction and then continue your learning by searching online for other resources if you need
# them: https://www.w3schools.com/python/python_sets.asp.
# As well as the code, submit 1 example in your write-up of sets A and B and the outputted values
# for a)-c).

# -------------------------- SAME CODE USING FUNCTIONS -----------------------------

def set_checker(list_one, list_two):
    # converts the lists to sets
    set_A = set(list_one)
    set_B = set(list_two)

    # checking A - B
    set_difference = set_A.difference(set_B)
    print("\nA - B: {}".format(set_difference))
    print("")

    # checking B ⊆ A
    subset = set_B.issubset(set_A)
    print("B ⊆ A: {}".format(subset))  # returns either true or false
    print("")

    # checking A x B
    for i in list_one:
        for j in list_two:
            new_set = {i, j}
            print(new_set)


# Test Data
list_A = [1, 2, 4]
list_B = [5, 4, 6]
set_checker(list_A, list_B)

# Using user input to run the program
# a = [int(item) for item in input("Enter the values for A").split()]
# b = [int(item) for item in input("Enter the values for B").split()]
# set_checker(a, b)
