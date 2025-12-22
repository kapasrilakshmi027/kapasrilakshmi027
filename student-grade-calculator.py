name=input("Enter student name: ")

m1=int(input("Enter subject 1 marks: "))
m2=int(input("Enter subject 2 marks: "))
m3=int(input("Enter subject 3 marks: "))
m4=int(input("Enter subject 4 marks: "))
m5=int(input("Enter subject 5 marks: "))

total_marks=m1+m2+m3+m4+m5
percentage=(total_marks/500)*100

if percentage>=90:
    Grade="A"
elif percentage>=75:
    Grade="B"
elif percentage>=60:
     Grade="C"
else:
     Grade="Fail"


print("\n-----STUDENT GRADE CALCULATOR-----")
print("name:",name)
print("Total Marks:",total_marks)
print("Percentage:",percentage)
print("Grade:",Grade)
