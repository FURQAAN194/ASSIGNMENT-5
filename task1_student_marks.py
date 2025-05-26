# Task 1: Dictionary of Student Marks

# Creating a dictionary with student names and their marks
student_marks = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "David": 67,
    "Eve": 90
}

# Asking the user to input a student's name
student_name = input("Enter the student's name: ")

# Retrieving and displaying the corresponding marks
if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print("Student not found in the record.")
