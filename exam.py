import json  # Import JSON module for saving/loading data

# Define the Person class to hold basic person information
class Person:
    def __init__(self, name, age, address):  # Initialize Person attributes
        self.name = name  # Set person's name
        self.age = age  # Set person's age
        self.address = address  # Set person's address

    def display_person_info(self):  # Display person's information
        print(f"Name: {self.name}, Age: {self.age}, Address: {self.address}")

# Define Student class inheriting from Person
class Student(Person):
    def __init__(self, name, age, address, student_id):  # Initialize Student attributes
        super().__init__(name, age, address)  # Initialize inherited attributes
        self.student_id = student_id  # Set student's unique ID
        self.grades = {}  # Initialize empty dictionary for grades
        self.courses = []  # Initialize empty list for courses

    def add_grade(self, subject, grade):  # Add or update grade for a subject
        self.grades[subject] = grade

    def enroll_course(self, course):  # Enroll student in a course
        self.courses.append(course)

    def display_student_info(self):  # Display student's information
        self.display_person_info()  # Display inherited person info
        print(f"ID: {self.student_id}, Courses: {self.courses}, Grades: {self.grades}")

# Define Course class to manage course information
class Course:
    def __init__(self, course_name, course_code, instructor):  # Initialize Course attributes
        self.course_name = course_name  # Set course name
        self.course_code = course_code  # Set course code
        self.instructor = instructor  # Set instructor's name
        self.students = []  # Initialize empty list for enrolled students

    def add_student(self, student):  # Add student to course
        self.students.append(student)

    def display_course_info(self):  # Display course details
        print(f"Course Name: {self.course_name}, Code: {self.course_code}, Instructor: {self.instructor}")
        print("Enrolled Students:", [student.name for student in self.students])

# Define StudentManagementSystem class to handle system operations
class StudentManagementSystem:
    def __init__(self):  # Initialize the system with empty dictionaries
        self.students = {}  # Dictionary to store students by ID
        self.courses = {}  # Dictionary to store courses by code

    def add_student(self, name, age, address, student_id):  # Add a new student
        student = Student(name, age, address, student_id)
        self.students[student_id] = student  # Add student to dictionary
        print(f"Student {name} (ID: {student_id}) added successfully.")

    def add_course(self, course_name, course_code, instructor):  # Add a new course
        course = Course(course_name, course_code, instructor)
        self.courses[course_code] = course  # Add course to dictionary
        print(f"Course {course_name} (Code: {course_code}) created with instructor {instructor}.")

    def enroll_student_in_course(self, student_id, course_code):  # Enroll student in a course
        student = self.students.get(student_id)
        course = self.courses.get(course_code)
        if student and course:  # Check if both student and course exist
            student.enroll_course(course.course_name)  # Enroll in course
            course.add_student(student)  # Add student to course
            print(f"Student {student.name} (ID: {student_id}) enrolled in {course.course_name} (Code: {course_code}).")
        else:
            print("Error: Invalid student ID or course code.")

    def add_grade(self, student_id, course_code, grade):  # Add grade for student
        student = self.students.get(student_id)
        course = self.courses.get(course_code)
        if student and course and course.course_name in student.courses:  # Ensure student is enrolled in course
            student.add_grade(course.course_name, grade)  # Assign grade
            print(f"Grade {grade} added for {student.name} in {course.course_name}.")
        else:
            print("Error: Student is not enrolled in the specified course.")

    def display_student_details(self, student_id):  # Display student details
        student = self.students.get(student_id)
        if student:
            student.display_student_info()
        else:
            print("Error: Student not found.")

    def display_course_details(self, course_code):  # Display course details
        course = self.courses.get(course_code)
        if course:
            course.display_course_info()
        else:
            print("Error: Course not found.")

    def save_data(self, filename="data.json"):  # Save data to file
        data = {
            "students": {sid: {
                "name": s.name, "age": s.age, "address": s.address,
                "grades": s.grades, "courses": s.courses
            } for sid, s in self.students.items()},
            "courses": {ccode: {
                "course_name": c.course_name, "instructor": c.instructor,
                "students": [s.student_id for s in c.students]
            } for ccode, c in self.courses.items()}
        }
        with open(filename, 'w') as file:
            json.dump(data, file)  # Save data as JSON
        print("All student and course data saved successfully.")

    def load_data(self, filename="data.json"):  # Load data from file
        try:
            with open(filename, 'r') as file:
                data = json.load(file)  # Load JSON data
            self.students = {sid: Student(d["name"], d["age"], d["address"], sid)
                             for sid, d in data["students"].items()}
            for sid, s_data in data["students"].items():
                student = self.students[sid]
                student.grades = s_data["grades"]
                student.courses = s_data["courses"]
            self.courses = {ccode: Course(d["course_name"], ccode, d["instructor"])
                            for ccode, d in data["courses"].items()}
            for ccode, c_data in data["courses"].items():
                course = self.courses[ccode]
                for sid in c_data["students"]:
                    student = self.students[sid]
                    course.add_student(student)
            print("Data loaded successfully.")
        except FileNotFoundError:
            print("Error: File not found.")

# Define main function for CLI
def main():
    system = StudentManagementSystem()  # Initialize the system
    while True:
        print("\n==== Student Management System ====")
        print("1. Add New Student")
        print("2. Add New Course")
        print("3. Enroll Student in Course")
        print("4. Add Grade for Student")
        print("5. Display Student Details")
        print("6. Display Course Details")
        print("7. Save Data to File")
        print("8. Load Data from File")
        print("0. Exit")
        choice = input("Select Option: ")

        if choice == '1':
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            address = input("Enter Address: ")
            student_id = input("Enter Student ID: ")
            system.add_student(name, age, address, student_id)
        elif choice == '2':
            course_name = input("Enter Course Name: ")
            course_code = input("Enter Course Code: ")
            instructor = input("Enter Instructor Name: ")
            system.add_course(course_name, course_code, instructor)
        elif choice == '3':
            student_id = input("Enter Student ID: ")
            course_code = input("Enter Course Code: ")
            system.enroll_student_in_course(student_id, course_code)
        elif choice == '4':
            student_id = input("Enter Student ID: ")
            course_code = input("Enter Course Code: ")
            grade = input("Enter Grade: ")
            system.add_grade(student_id, course_code, grade)
        elif choice == '5':
            student_id = input("Enter Student ID: ")
            system.display_student_details(student_id)
        elif choice == '6':
            course_code = input("Enter Course Code: ")
            system.display_course_details(course_code)
        elif choice == '7':
            system.save_data()
        elif choice == '8':
            system.load_data()
        elif choice == '0':
            print("Exiting Student Management System. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# Run main function if script is executed directly
if __name__ == "__main__":
    main()
