"""

Instructions

You are going to write a program that calculates the average student height from a List of heights.

e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]

The average height can be calculated by adding all the heights together and dividing by the total number of heights.

e.g.

180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146

There are a total of 7 heights in student_heights

1146 ÷ 7 = 163.71428571428572

Average height rounded to the nearest whole number = 164

Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.

156 178 165 171 187

In this case, student_heights would be a list that looks like: [156, 178, 165, 171, 187]
Example Output

171


"""

# solution

students_heights = input("Input a list of student heights: ").split()
sum = 0
length = 0
no_of_students =0

for n in range(0, len(students_heights)):
    students_heights[n] = int(students_heights[n])
print(students_heights)

for student in students_heights:
    sum += student
    no_of_students += 1

average = round(sum / no_of_students)
print(f"Average student height is {average}")



    