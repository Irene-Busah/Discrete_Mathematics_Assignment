# Question 4
A = [item for item in input("Please the values for list A:").split()]
# Setting the list size for R
list_size_R = 2
values_input = int(input("Please enter the number of times you are going to input values:"))
R = []
values_r = [[int(input("Enter a value")) for _ in range(list_size_R)]]
R.append(values_r)
R = set(R)
print("R is a set")
# performing cartesian product of  A X A
product_A = []
for i in A:
    for j in A:
        answer = (i, j)
        product_A.append(answer)
print("Product of A x A is = ")
product_A = set(product_A)
print(product_A)
# # Checking if R is a subset of A x A
possible_R_subset_A = R.issubset(product_A)
print(possible_R_subset_A)
