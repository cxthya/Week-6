'''
Cinthya Calderon-Hernandez
CMSC 111
Spring 2026
Assignment 2: Working with Tuples
'''
#Task 1 Creat a tuple with 3 cities
cities = ("tokyo", "milan", "cairo")
print(cities)

#Task 2 Access a second city
second_city = cities[1]
print("The second city is:", second_city)

#Task 3 Attempt to modify tuple - expected error code
cities[0] = "paris"  # This will raise a TypeError since tuples are immutable
print(cities)