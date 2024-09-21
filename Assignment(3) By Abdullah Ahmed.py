# Defining the Person class with properties and a display_info() method
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def display_info(self):
        print(f"First Name: {self.first_name}, Last Name: {self.last_name}, Age: {self.age}")

# Defining the Student class inheriting from Person with additional properties and a display_info() method
class Student(Person):
    def __init__(self, first_name, last_name, age, student_id, gpa):
        super().__init__(first_name, last_name, age)
        self.student_id = student_id
        self.gpa = gpa

    def display_info(self):
        # Overriding to display both Person and Student properties
        super().display_info()
        print(f"Student ID: {self.student_id}, GPA: {self.gpa}")

# Defining the Teacher class inheriting from Person with additional properties and a display_info() method
class Teacher(Person):
    def __init__(self, first_name, last_name, age, teacher_id, salary):
        super().__init__(first_name, last_name, age)
        self.teacher_id = teacher_id
        self.salary = salary

    def display_info(self):
        # Overriding to display both Person and Teacher properties
        super().display_info()
        print(f"Teacher ID: {self.teacher_id}, Salary: ${self.salary}")

# Example instance of Student class
student_instance = Student("Burhan", "Fasih", 17, "112233", 3.8)
# Calling the display_info method of the Student instance
student_instance.display_info()

# Example instance of Teacher class
teacher_instance = Teacher("Abdullah", "Ahmed", 25, "786123", 60000)
# Calling the display_info method of the Teacher instance
teacher_instance.display_info()
