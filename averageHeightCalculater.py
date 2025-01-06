# Write a porgram that calxulates the average student from the list of heights.

student_heights = input("Input a list of sutdent heights.\n > ").split()
# print(student_heights)
for n in range(0,len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

sum = 0
i = 0
for individual_height in student_heights:
    sum = sum + individual_height
    i = i + 1
average_height = sum / i
print(f"The average height of given students is {average_height}")