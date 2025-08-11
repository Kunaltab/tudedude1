student_marks={"Alice":90}
name = input("Enter the student name :")
if name in student_marks:
    print(f"{name}'s marks:{student_marks[name]}")
else:
    print ("student not found ")
 