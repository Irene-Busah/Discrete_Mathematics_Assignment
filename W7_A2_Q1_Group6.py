# Write a programme to test if a given list of elements constitutes a set. It should take as its input a
# list of elements and should output a True or False value.
# If the truth value is False then it must also output the list converted to a set or to a list which
# represents the set.

# get user input into a list variable
list_names = [item for item in input("Enter the names of the first 5 best students: ").split()]
print(list_names)
# convert the list into a set
set_names = set(list_names)
# Condition to check if the list contains an element appearing twice by comparison to the set created from the list
if len(list_names) != len(set_names):
    new_set_names = list(set_names)
    print("False, the set should be: " + str(new_set_names))
elif len(list_names) == len(set_names):
    print("True")
