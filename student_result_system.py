# Functions based Student Result System

def student_details():
    name=input("Enter student name: ")
    marks=[]

    for i in range(1, 6):
        mark=int(input(f"Enter marks for subject {i}: "))
        marks.append(mark)

    return name,marks


def calculate_total(marks):
    return sum(marks)


def calculate_percentage(total):
    return (total / 500) * 100


def assign_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "Fail"


def display_result(name, marks, total, percentage, grade):
    print("\n----- STUDENT RESULT -----")
    print("Name:", name)
    print("Marks:", marks)
    print("Total:", total)
    print(f"Percentage: {percentage:.2f}%")
    print("Grade:", grade)


def main():
    name, marks = student_details()
    total = calculate_total(marks)
    percentage = calculate_percentage(total)
    grade = assign_grade(percentage)
    display_result(name,marks,total,percentage,grade)


main()
