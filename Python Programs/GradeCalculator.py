# Create a program that calculates the grades of students based on their scores. Ask the user to input the scores of multiple students, and then calculate and display their grades (A, B, C, D, or F) based on the following criteria:

# A: 90 or above
# B: 80 - 89
# C: 70 - 79
# D: 60 - 69
# F: below 60


#Solution 1
# Function to calculate grade
def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# Input number of students
num_students = int(input("Enter the number of students: "))

# Initialize a dictionary to store student names and scores
student_scores = {}

# Input loop to get scores for each student
for i in range(1, num_students + 1):
    name = input(f"Enter the name of student {i}: ")
    score = float(input(f"Enter the score of student {i}: "))
    student_scores[name] = score

# Calculate and display grades for each student
print("\nGrades:")
for name, score in student_scores.items():
    grade = calculate_grade(score)
    print(f"{name}: {grade}")


#Solution 2
# Ask the user to input the scores of multiple students
num_students = int(input("Enter the number of students: "))

# Initialize an empty list to store the scores and grades
student_data = []

# Input loop for each student
for i in range(num_students):
    score = float(input(f"Enter the score for student {i + 1}: "))

    # Calculate the grade based on the score
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'

    # Append the score and grade to the list
    student_data.append((score, grade))

# Display the grades of each student
print("\nStudent Grades:")
for i, (score, grade) in enumerate(student_data):
    print(f"Student {i + 1}: Score = {score}, Grade = {grade}")



#Solution 3
# Ask the user to input the scores of multiple students
num_students = int(input("Enter the number of students: "))

# Initialize an empty list to store the scores and grades
student_scores = []
student_grades = []

# Input loop for each student
for i in range(num_students):
    score = float(input(f"Enter the score for student {i + 1}: "))

    # Calculate the grade based on the score
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'

    # Append the score and grade to the list
    student_score.append(score)
    student_grade.append(grade)

# Display the grades of each student
print("\nStudent Grades:")
for i in range(num_students):
    print(f"Student {i+1}: Score = {scores[i]}, Grade = {grades[i]}")