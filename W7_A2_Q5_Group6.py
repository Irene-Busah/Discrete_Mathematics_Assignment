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
            if y % x == 0:
                print(f'{y} / {x} = {True}')
            else:
                print(f'{y} / {x} = {False}')


lst_one = [3, 5, 7]
lst_two = [8, 4, 10]

proper_subset(lst_one, lst_two)
