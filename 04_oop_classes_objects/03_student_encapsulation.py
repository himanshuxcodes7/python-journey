class Student:
    def __init__(self, name, roll_no, marks):
        self._name = name
        self._roll_no = roll_no
        self._marks = marks

# Getter for name
    def get_name(self):
        return self._name

# Setter for name
    def set_name(self, name):
        if not name or not name.strip():
            print("Name cannot be empty!")
        else:
            self._name = name
            print("Name updated successfully!")

# Getter for roll number
    def get_roll_no(self):
        return self._roll_no

# Setter for roll number
    def set_roll_no(self, roll_no):
        if not isinstance(roll_no, int) or not 1 <= roll_no <= 100:
            print("Roll number must be between 1 and 100!")
        else:
            self._roll_no = roll_no
            print("Roll number updated successfully!")

# Getter for marks
    def get_marks(self):
        return self._marks

# Setter for marks
    def set_marks(self, marks):
        if not isinstance(marks, (int, float)) or marks < 0:
            print("Marks cannot be negative and must be numeric!")
        else:
            self.marks = marks
            print("Marks updated successfully!")   

student1 = Student("Rahul", 15, 85)                                              

print(f"Name: {student1.get_name()}")
print("Roll Number:", student1.get_roll_no())
print("Marks:", student1.get_marks())

student1.set_name("Aman")
student1.set_roll_no(25)
student1.set_marks(92)

print("\nAfter updating:")
print("Name:", student1.get_name())
print("Roll Number:", student1.get_roll_no())
print("Marks:", student1.get_marks())