#user input
name=input("Enter student name: ")
roll_number=int(input("Enter roll number: "))
#list implementation
marks=[]
marks.append(int(input("enter subject 1 marks: ")))
marks.append(int(input("enter subject 2 marks: ")))
marks.append(int(input("enter subject 3 marks: ")))
marks.append(int(input("enter subject 4 marks: ")))
marks.append(int(input("enter subject 5 marks: ")))
marks.append(int(input("enter subject 6 marks: ")))
#tuple implementation
total_marks=sum(marks)
average_marks=total_marks/len(marks)
#sets implementation
student_profile={
    "Name":name,
    "Roll Number":roll_number,
    "Marks":marks,
    "Total marks":total_marks,
    "Average marks":average_marks
}
#output of the data
print("\n-----STUDENT PROFILE MANAGER-----")
print("Name:",name)
print("Roll Number:",roll_number)
print("Marks:",marks)
print("Total Marks:",total_marks)
print("Average Marks:",average_marks)
