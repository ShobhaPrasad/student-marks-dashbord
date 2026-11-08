# Count no. of Students
totalstudent=int(input("enter no. of student \t"))

# Data Store
studentdata=[]

# Inserting Data 
for i in range(totalstudent):
    print(f"enter the student {i+1}")
    name=input("\tEnter Name \n")
    roll=int(input("\t Enter Roll \n"))
    marks=int(input(" \t Enput marks\n "))

    if marks>=90:
         grade="+A"
    elif marks >=70:
        grade="A"
    elif marks>59:
        grade="B"
    elif marks >49:
        grade="C"
    else:
        grade="F"

# creating 

    student={
    "name":name,
    "roll":roll,
    "marks":marks,
    "grade":grade
 }

    studentdata.append(student)
# append use for add items  in the list , we are adding student


print("All student Data :\n")
for s in studentdata:
    print(f"name = {s['name']}  |  roll = {s['roll']}  | mark = {s['marks']} | grade = {s['grade']}")
