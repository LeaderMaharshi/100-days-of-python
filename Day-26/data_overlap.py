""" 
Instructions

Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.

You are going to create a list called result which contains the numbers that are common in both files.

e.g. if file1.txt contained:

1
2
3

and file2.txt contained:

2
3
4

result = [2, 3]

IMPORTANT: The result should be a list that contains Integers, not Strings. Try to use List Comprehension instead of a Loop.
Example Output

[3, 6, 5, 33, 12, 7, 42, 13]

Hint

    Use the keyword method for starting the List comprehension and fill in the relevant parts.
    First, you will need to read from the files and create a list using the lines in the files.
    This method will be really useful: https://www.w3schools.com/python/ref_file_readlines.asp
    Remember you can check if a value exists in a list using the in keyword. https://www.w3schools.com/python/ref_keyword_in.asp
    Remember you can convert a string to an int using the int() method. https://www.w3schools.com/python/ref_func_int.asp



"""

with open("Day-26/file1.txt") as file1:
    list1 = file1.readlines()
    
with open("Day-26/file2.txt") as file2:
    list2 = file2.readlines() 
    
result = [int(num) for num in list1 if num in list2]
print(result)