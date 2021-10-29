# Write a programme that takes as input 2 finite sets or lists (you decide) X and Y , where X, Y ⊂ Z,
# and outputs a truth value (’True’ or ’False’) for the following statement:
# ∀x ∈ X, ∃y ∈ Y such that y | x.
# In addition to the code, give 1 example in your write-up of sets X, Y where this truth value is
# True, and 1 example where the truth value is False.

def proper_subset(set_X, set_Y):
    # set_Z = {1, 2, 3, ...}        #  the set X and set Y are a set of integers, i.e, proper subset of Z
    set_1 = set(set_X)
    set_2 = set(set_Y)
    if set_2 < set_1:
        return True
    else:
        return False


list_X = input("Enter the set X: ")
list_Y = input("Enter the set Y: ")
result = proper_subset(list_X, list_Y)
print(result)
