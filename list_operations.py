'''
Cinthya Calderon-Hernandez
CMSC 111
Spring 2026
Assignment 1: Working with Lists
'''

#Task 1 Creating a list of integerrs 1-10 and printing the original list
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list1)

#Task 2 Modify the list by adding 11 and removing 5
list1.append(11)
list1.remove(5)
print("Updated list:", list1)

#Task 3 Slice the first 5 elements of updated list 
placed_list = list1[:5]
print("Sliced list:", placed_list)

#except and try code 
try: 
    list1.remove(5)
except ValueError:
    print("5 is not in the list, cannot remove it.")
print ("Final list:", list1)
    

