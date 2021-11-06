# Write a programme that takes as input 2 finite sets or lists (you decide) X and Y , where X, Y ⊂ Z,
# and outputs a truth value (’True’ or ’False’) for the following statement:
# ∀x ∈ X, ∃y ∈ Y such that y | x.
# In addition to the code, give 1 example in your write-up of sets X, Y where this truth value is
# True, and 1 example where the truth value is False.


# # ∀x ∈ X, ∃y ∈ Y such that y | x ==> for each input, check if the all the elements x that belongs to the set X,
# and some elements y that belongs to the set Y, such that y is divisible by x (? y / x)
# X is a list [...], Y is also a list [....]
# elements in both list (set) must be integers
# return value should be True or False


def proper_subset(set_X, set_Y):

    for y in set_Y:
        for x in set_X:
            if x / y == 0:
                # print(f'{y} / {x} = {True}')
                return True
            elif x / y != 0:
                # print(f'{y} / {x} = {False}')
                return False

# Test data
lst_one = [4, 8, 2]
lst_two = [3, 7, 11]

print(proper_subset(lst_one, lst_two))

# # Suggested extra code for how the program would work using user input
# user_input_X = input("Please enter the values for list X:").split(",")
# user_input_Y = input("Please enter the values for list Y:").split(",")
# # Converts user input into an int and adds them to the list
# lst_one_X = [int(i) for i in user_input_X]
# lst_two_Y = [int(i) for i in user_input_Y]
# print(proper_subset(lst_one_X, lst_two_Y))
