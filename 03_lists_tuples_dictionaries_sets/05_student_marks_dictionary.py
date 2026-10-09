students = {
    "Rahul" : 84,
    "Kunal" : 74,
    "Priyesh" : 45
}

print("\n--- Student Marks Management ---")
print("A - Add a student")
print("B - Update marks")
print("C - Search for a student")
print("D - Display all student and marks")

choice = input("Enter your choice: A/B/C/D : ").upper()

if choice == "A":
    name = input("Enter student name: ").strip()
    if name in students:
        print("Name already exist")
    else:
        marks = int(input("enter marks: "))
        students[name] = marks
        print("Student added successfully!")
elif choice == "B":
    name = input("Enter student name: ").strip()
    if name in students:
        marks = int(input("Enter marks for student: "))
        students[name] = marks
        print("Marks updated successfully!")
    else:
        print("Student not found")
elif choice == "C":
    name = input("Enter name of student: ").strip()
    if name in students:
        print(f"{name}'s marks: {students[name]}")
    else:
        print("Student not found")
elif choice == "D":
    for name, marks in students.items():
        print(f"{name} : {marks}")
else:
    print("Invalid Input entered")                    



