student_name=input("Enter student name: ")

Telugu=int(input("Enter Telugu Marks: "))
Hindi=int(input("Enter Hindi Marks: "))
English=int(input("Enter English Marks: "))
Mathematics=int(input("Enter Mathematics Marks: "))
PhysicalScience=int(input("Enter PhysicalScience Marks: "))
Social=int(input("Enter Social Marks: "))

total_marks=Telugu+Hindi+English+Mathematics+PhysicalScience+Social

percentage=(total_marks/600)*100

print("\n-----STUDENT RESULT-----")
print("Name:",student_name)
print("Total marks:",total_marks)
print("Percentage:",percentage)
