"""Enter name and marks in 6 subjects of a student and find the total, average and percentage."""

name=input("Enter the name of the student: ")
m1=float(input("Enter the marks in subject 1: "))
m2=float(input("Enter the marks in subject 2: "))
m3=float(input("Enter the marks in subject 3: "))
m4=float(input("Enter the marks in subject 4: "))
m5=float(input("Enter the marks in subject 5: "))
m6=float(input("Enter the marks in subject 6: "))
total=m1+m2+m3+m4+m5+m6
average=total/6
percentage=(total/600)*100
print("The total marks are: ",total)
print("The average marks are: ",average)
print("The percentage is: ",percentage)