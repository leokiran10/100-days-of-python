# You have access to a datebase of student_scores in format of dictonary. Write a program that converts their scores to grades.

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}
grade = ""
for thing in student_scores:
    if student_scores[thing] >= 91:
        grade = "Outstanding"
    elif student_scores[thing] >= 81:
        grade = "Exceeds Expectations"
    elif student_scores[thing] >= 71:
        grade = "Acceptable"
    else:
        grade = "Fail"
    
    student_grades[thing] = grade

print(student_grades)