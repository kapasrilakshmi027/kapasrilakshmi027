#useer input
name=input("Enter student name: ")
#student marks
m1=(input("Enter subject 1 marks: "))
m2=(input("Enter subject 2 marks: "))
m3=(input("Enter subject 3 marks: "))
#before type conversion
print("\n-----DATA TYPES BEFORE CONVERSION-----")
print(type(m1),type(m2),type(m3))
#string to in conversion
m1=int(m1)
m2=int(m2)                
m3=int(m3)
#after type conversion
print("\n-----DATA TYPES AFTER CONVERSION-----")
print(type(m1),type(m2),type(m3))
#calculation
total_marks=m1+m2+m3                
percentage=float((total_marks/300)*100)
#student result output
print("\n-----STUDENT RESULTS-----")
print("Name: ",name)
print("Total Marks: ",total_marks)
print("Percentage: ",percentage)
print("Percentage Type: ",type(percentage))                
