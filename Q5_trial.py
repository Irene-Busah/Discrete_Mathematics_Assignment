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

def checkIfSet(R):
    count = 0
    for item in R:
        for subset in R:
            if item == subset:
                count += 1
        if count == 2:
            return 'R is not a set'
        else:
            count = 0

    return 'R is a set'


def contains_all(A, R):
    for item in R:
        if item[0] not in A or item[1] not in A:
            return "R is not a subset of A"

    return 'R is a subset of A'


def check_Relation(A, R):
    for item in R:
        if item[0] not in A or item[1] not in A:
            return "R is not a relation"

    return 'R is a relation on A'


def reflexive(R, A):
    """Returns True if a relation R on set A is reflexive, False otherwise."""
    for a in A:
        list_relation = [a, a]
        if list_relation not in R:
            print('R is not reflexive : ' + str(a))


def symmetric(R, A):
    for a, b in R:
        templist = [a, b]
        templist2 = [b, a]
        if templist2 not in R:
            return 'R is not symmetric : ' + str(templist)


def is_transitive(f, domain):
    for i in domain:
        for j in domain:
            for k in domain:
                subset_a = [i, j]
                subset_b = [j, k]
                subset_c = [i, k]
                if subset_a in f and subset_b in f and subset_c not in f:
                    return "R is not transitive : " + str(subset_a)

    return "transitive"


# if __name__ == "_main_":
#     A = [1, 3, 4, 5]
#     R = [[1, 1], [1, 5], [5, 1], [5, 5], [3, 4], [4, 1], [4, 4]]

A = [1, 3, 4, 5]
R = [[1, 1], [1, 5], [5, 1], [5, 5], [3, 4], [4, 1], [4, 4]]
print(checkIfSet(R))
print(contains_all(A, R))
print(check_Relation(A, R))
reflexive(R, A)
print(symmetric(R, A))
print(is_transitive(R, A))


# A = [1, 3, 4, 5]
# R = [[1, 1], [1, 5], [5, 1], [5, 5], [3, 4], [4, 1], [4, 4]]
# def symmetric(R, A):
#     for a, b in R:
#         templist = [a, b]
#         templist2 = [b, a]
#         if templist2 and templist not in R:
#             return 'R is not symmetric : ' + str(templist)
#         else:
#             return 'R is symmetric : ' + str(templist)
# print(symmetric(R, A))


# A = [1, 3, 4, 5]
# R = [[1, 1], [1, 5], [5, 1], [5, 5], [3, 4], [4, 1], [4, 4]]
# product_a = []
# for i in A:
#     for j in A:
#         product_a.append([i, j])
#         print(product_a)
#     # return product_a
# def symmetric(R, product_a):
#     for [a, b] in product_a:
#         templist = [a, b]
#         templist2 = [b, a]
#         if templist2 and templist not in R:
#             return 'R is not symmetric : ' + str(templist)
#         else:
#             return 'R is symmetric : '
# print(symmetric(R, product_a))

def symmetric(list_r_2):
    not_present = []
    # print("check o")
    for x in list_r_2:
        for y in list_r_2:
            for z in list_r_2:
                # print("Check 1")
                if x[1] == y[0] and y[1] == z[1] and x[0] == z[0] and x not in list_r_2 and y not in list_r_2:
                    print("check 2")
                elif x[1] == y[0] and y[1] != z[1] and x[0] != z[0]:
                    not_present.append(z)

    if not_present == []:
        print("R is transitive")
    else:
        print("R is not transitive", not_present)


symmetric(list_r_2)
