
# Day 4: Enhanced Personal Information Program

print("=" * 60)
print("            STUDENT PROFILE AND RESULT SYSTEM")
print("=" * 60)

name = input("\nEnter student name: ")
roll_number = input("Enter roll number: ")
course = input("Enter course name: ")
college = input("Enter college name: ")

print("\nEnter marks out of 100:")

python_marks = float(input("Python marks: "))
math_marks = float(input("Mathematics marks: "))
computer_marks = float(input("Computer Science marks: "))
english_marks = float(input("English marks: "))
communication_marks = float(input("Communication marks: "))

total = (
    python_marks
    + math_marks
    + computer_marks
    + english_marks
    + communication_marks
)

percentage = total / 5

print("\n" + "-" * 60)
print("                 STUDENT REPORT")
print("-" * 60)

print(f"Student Name : {name}")
print(f"Roll Number  : {roll_number}")
print(f"Course       : {course}")
print(f"College      : {college}")

print("\nSubject-wise Marks:")
print(f"Python             : {python_marks}/100")
print(f"Mathematics        : {math_marks}/100")
print(f"Computer Science   : {computer_marks}/100")
print(f"English            : {english_marks}/100")
print(f"Communication      : {communication_marks}/100")

print("\nTotal Marks:", total, "/ 500")
print(f"Percentage: {percentage:.2f}%")

if max(
    python_marks,
    math_marks,
    computer_marks,
    english_marks,
    communication_marks
) > 100 or min(
    python_marks,
    math_marks,
    computer_marks,
    english_marks,
    communication_marks
) < 0:
    print("Invalid marks! Enter marks between 0 and 100.")

elif min(
    python_marks,
    math_marks,
    computer_marks,
    english_marks,
    communication_marks
) < 35:
    print("Result: FAIL")
    
elif percentage >= 75:
    print("Result: PASS - DISTINCTION")
elif percentage >= 60:
    print("Result: PASS - FIRST CLASS")
elif percentage >= 35:
    print("Result: PASS")

print("\nThank you for using the Student Result System.")
print("=" * 60)
