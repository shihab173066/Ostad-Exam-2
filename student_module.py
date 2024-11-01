from person_module import *

class Student(Person):
    def __init__(self, name, age, address, student_id):
        super().__init__(name, age, address)
        self.student_id = student_id           # Unique student identifier
        self.grades = {}                       # Dictionary to store grades by subject
        self.courses = []                      # List to store enrolled courses

    def add_grade(self, subject, grade):
        # Adds or updates grade for specified subject
        self.grades[subject] = grade
        print(f"Grade {grade} added for {self.name} in {subject}")

    def enroll_course(self, course):
        # Enroll student in a course
        if course not in self.courses:
            self.courses.append(course)
            print(f"{self.name} enrolled in {course}")

    def display_student_info(self):
        # Display all student details
        super().display_person_info()
        print(f"Student ID: {self.student_id}")
        print(f"Courses Enrolled: {self.courses}")
        print(f"Grades: {self.grades}")
