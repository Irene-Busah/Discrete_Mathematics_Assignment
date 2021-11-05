# Question 4
# Input list R
# Number of sub lists

list_size = 2
num_list = int(input("Please enter the number of sublist you will input: "))
list_r = [[int(input("Please enter a single number and press enter: ")) for _ in range(list_size)]
          for _ in range(num_list)]
print(list_r)


# Input the list A


# Checking if R is a set by checking if the list R has any duplicates
def checking_duplicatesR():
    """Checking if the given list R contains any duplicates"""
    if len(list_r) == len(set(list_r)):
        print("R is a set")

    else:
        print("R is not a set")


def cartesian_product_A():
    """Input the list A and perform the cartesian product of A"""
    list_a = [item for item in input("Please the values for list A:").split()]
    product_a = []
    for i in list_a:
        for j in list_a:
            answer = (i, j)
            product_a.append(answer)

