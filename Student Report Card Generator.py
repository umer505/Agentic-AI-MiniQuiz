students = {
    "ali": {
        "rollNo": 101,
        "marks": [80, 90, 85, 88, 92]
    },
    "fatima": {
        "rollNo": 102,
        "marks": [78, 82, 84, 90, 88]
    },
    "ahmed": {
        "rollNo": 103,
        "marks": [75, 80, 78, 85, 82]
        },
    "sara": {
        "rollNo": 104,
        "marks": [88, 92, 90, 85, 87]
    },
    "zain": {
        "rollNo": 105,
        "marks": [95, 90, 92, 88, 94]
    },
    "aisha": {
        "rollNo": 106,
        "marks": [82, 85, 88, 90, 84]
    },
    "hassan": {
        "rollNo": 107,
        "marks": [80, 78, 85, 82, 88]
    }
}


def calculate_average(marks):
    return sum(marks) / len(marks) if marks else 0

def total_marks(marks):
    return sum(marks) if marks else 0

def generate_report_card(student_name):
    student = students.get(student_name)
    if not student:
        return f"Student {student_name} not found."

    roll_number = student["rollNo"]
    marks = student["marks"]
    average_marks = calculate_average(marks)
    
    if average_marks >= 90:
        grade = 'A'
    elif average_marks >= 80:
        grade = 'B'
    elif average_marks >= 70:
        grade = 'C'
    elif average_marks >= 60:
        grade = 'D'
    else:
        grade = 'F'
    
    report_card = f" Report Card for {student_name} (Roll No: {roll_number})\n"
    report_card += "----------------------------------------\n"
    report_card += f"Student Name: {student_name}\n"
    report_card += f"Roll Number: {roll_number}\n"
    report_card += f"Marks: {marks}\n"
    report_card += f"Total Marks: {total_marks(marks)}\n"
    report_card += f"Average Marks: {average_marks}\n"
    report_card += f"Grade: {grade}\n"
    report_card += "----------------------------------------\n"

    return report_card

print("Welcome to the Student Report Card Generator!")
while True:
    student_name = input("Enter the student's name (or 'exit' to quit): ").strip()
    if student_name.lower() == 'exit':
        print("Exiting the report card generator. Goodbye!")
        break
    report_card = generate_report_card(student_name)
    print(report_card)