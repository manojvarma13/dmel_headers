#!/usr/bin/env python
# variables.py
# A variable containing a string
my_name = 'Sai Manoj'

# A variable containing an integer
my_age = 25

# A list of strings
friends_names = ["Sai Manoj", "Pragnya Chavali", "Mariya Syed"]

# A list of numbers
random_numbers = [17.2, 83.2, 45, 1000]

# A dictionary of names and ages
ages = {'Sai Manoj': 25, 'Pragnya Chavali': 24, 'Mariya Syed': 24}

# Print the values of the variables
print(my_name)
print(my_age)
print(friends_names)
print(random_numbers)
print(ages)

# Find out what type Python assigned to the variables
print(type(my_name))
print(type(my_age))
print(type(friends_names))
print(type(random_numbers))
print(type(ages))

# Iterate over names in a for loop
for name in friends_names:
    print(name)
    print(type(name))
