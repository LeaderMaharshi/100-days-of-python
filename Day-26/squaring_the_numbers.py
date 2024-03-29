"""
Instructions

You are going to write a List Comprehension to create a new list called squared_numbers. This new list should contain every number in the list numbers but each number should be squared.

e.g. 

4 * 4 = 16

4 squared equals 16.

"""

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [num * num for num in numbers]
print(squared_numbers)