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

    for x in set_X:
        for y in set_Y:
            if x % y == 0:
                # print(f'{y} / {x} = {True}')
                return True
            elif x % y != 0:
                # print(f'{y} / {x} = {False}')
                return False


lst_one = [4, 8, 2]
lst_two = [4, 3, 11]    # an element (2) in set Y can divides all the elements of set X
print(proper_subset(lst_one, lst_two))    # RETURN TRUE

lst_x = [4, 8, 2]
lst_y = [5, 3, 11]    # no element in set Y can divide any or all the elements of set X
print(proper_subset(lst_x, lst_y))  # RETURN FALSE
