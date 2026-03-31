'''
Cinthya Calderon-Hernandez
CMSC 111
Spring 2026
Assignment 3: Working with Sets
'''

#Task 1 Create a set
numbers_set = {1, 2, 2, 3, 4,}
print("Set of numbers:", numbers_set)

#Task 2 Modify set by taking out duplicates and adding new number
numbers_set.add(5)
numbers_set.remove(2)
print("Updated set:", numbers_set)

#Task 3 Membership test to check if the number 2 is in the set
is_present = 4 in numbers_set
print("Is the number 4 in the set?", is_present)
