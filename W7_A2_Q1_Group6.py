# Write a programme to test if a given list of elements constitutes a set. It should take as its input a
# list of elements and should output a True or False value.
# If the truth value is False then it must also output the list converted to a set or to a list which
# represents the set.

# # get user input into a list variable
# list_names = [item for item in input("Enter the names of the first 5 best students: ").split()]
# print(list_names)
#
# # convert the list into a set
# set_names = set(list_names)
#
# # Condition to check if the list contains an element appearing twice by comparison to the set created from the list
# if len(list_names) != len(set_names):
#     new_set_names = list(set_names)
#     print("False, the set should be: " + str(new_set_names))
# elif len(list_names) == len(set_names):
#     print("True")

# ----------------------------- THE SAME CODE USING FUNCTION ----------------------------------------

def set_checker(list_names):
    # for item in list_one.split(","):
    print(list_names)
    set_names = set(list_names)

    if len(list_names) != len(set_names):
        new_set_names = list(set_names)
        # print("")
        print("False, the set should be: " + str(new_set_names))
    elif len(list_names) == len(set_names):
        print("True")


# ------------------- TEST CODE ----------------------------
names = ["Irene", "Myra", "Nelson", "Irene", "Nelson"]
set_checker(names)        # // RETURNS FALSE
print("")
list_one = ["Irene", "Micheal", "Nelson", "Myra", "King"]
set_checker(list_one)  # // RETURN TRUE
print("")
number = [1, 3, 5, 6, 1]
set_checker(number)   # // RETURN FALSE
print("")
number_list = ["Irene", 2, 4, "Myra"]
set_checker(number_list)     # // RETURN TRUE

