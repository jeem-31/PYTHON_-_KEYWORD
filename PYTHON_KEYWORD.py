"""
School Management System - Basic Python Keywords
This script simulates a simple school management system handling student attendance, assignments, and grades.
"""

# Logical operations to check if a student is eligible for exams
attendance = True  # 'True'
assignments_submitted = False  # 'False'
print("Eligible for exam:", attendance and assignments_submitted)  # 'and'
print("Needs improvement:", not assignments_submitted)  # 'not'

# Conditional statements to determine pass or fail status
grade = 75
if grade >= 90:
    print("Grade: A")  # 'if'
elif grade >= 75:
    print("Grade: B")  # 'elif'
else:
    print("Grade: F - Needs Improvement")  # 'else'

# Looping through students to check attendance
students = ["Alice", "Bob", "Charlie"]
for student in students:  # 'for'
    if student == "Bob":
        continue  # Skip Bob (example of 'continue')
    print("Checking attendance for:", student)
    if student == "Charlie":
        break  # Stop after checking Charlie (example of 'break')

# Function to calculate grades
def calculate_grade(score):  # 'def'
    global passing_grade  # 'global'
    passing_grade = 75
    return "Pass" if score >= passing_grade else "Fail"  # 'return'

print("Student Result:", calculate_grade(80))

# Exception handling for student data retrieval
try:
    student_scores = {"Alice": 85, "Bob": None}
    print("Bob's Score:", student_scores["Bob"])  # This may raise an error
    assert student_scores["Bob"] is not None  # 'assert'
except (TypeError, AssertionError) as e:  # 'except', 'as'
    print("Error handling student data:", e)
finally:
    print("Finished processing student records")  # 'finally'

# Student class definition
class Student:  # 'class'
    def __init__(self, name, age, grade):
        self.name = name  # 'self'
        self.age = age
        self.grade = grade

    def get_info(self):
        return f"Student: {self.name}, Age: {self.age}, Grade: {self.grade}"

student1 = Student("Alice", 20, "B")
print(student1.get_info())

# Nested functions with 'nonlocal' keyword
def update_attendance():
    status = "Absent"
    def mark_present():
        nonlocal status  # 'nonlocal'
        status = "Present"
    mark_present()
    print("Attendance Status:", status)

update_attendance()

# File handling - Storing student records
with open("students.txt", "w") as file:  # 'with'
    file.write("Alice - Grade: B\n")

# Deleting student record
del student1  # 'del'

# Checking if a variable is None
var = None  # 'None'
print("Is variable None?", var is None)  # 'is'

# Importing modules for additional operations
import math  # 'import'
from datetime import datetime  # 'from'

# Using a lambda function to compute square of a number
square = lambda x: x * x  # 'lambda'
print("Square of 5:", square(5))

# Generator function to yield students needing attendance follow-up
def attendance_follow_up():
    for student in students:
        yield f"Follow up with: {student}"  # 'yield'

gen = attendance_follow_up()
print(next(gen))
print(next(gen))
