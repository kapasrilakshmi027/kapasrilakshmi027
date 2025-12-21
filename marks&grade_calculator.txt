name=input("Enter student name: ")

marks=[]
m1=int(input("Enter subject 1 marks: "))
m2=int(input("Enter subject 2 marks: "))
m3=int(input("Enter subject 3 marks: "))
m4=int(input("Enter subject 4 marks: "))
m5=int(input("Enter subject 5 marks: "))
m6=int(input("Enter subject 6 marks: "))

total_marks=m1+m2+m3+m4+m5+m6
percentage=(total_marks/600)*100

if percentage>=90:
    grade='A'
elif percentage>=75:
    grade='B'
elif percentage>=70:
   grade='C'
elif percentage>=60:
   grade='D'
else:
    print("Fail")

print("\n-----STUDENT RESULT-----")
print("Name:",name)
print("Total Marks: ",total_marks)
print("Percentage: ",percentage)
print("Grade:",grade)
