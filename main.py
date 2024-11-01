from student_module import *
from course_module import *
from file_module import *

students = []
courses = []

def add_student():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    address = input("Enter Address: ")
    student_id = input("Enter Student ID: ")
    student = Student(name, age, address, student_id)
    students.append(student)
    print(f"Student {name} (ID: {student_id}) added successfully.")

def add_course():
    course_name = input("Enter Course Name: ")
    course_code = input("Enter Course Code: ")
    instructor = input("Enter Instructor Name: ")
    course = Course(course_name, course_code, instructor)
    courses.append(course)
    print(f"Course {course_name} (Code: {course_code}) created with instructor {instructor}.")

def enroll_student_in_course():
    student_id = input("Enter Student ID: ")
    course_code = input("Enter Course Code: ")
    student = next((s for s in students if s.student_id == student_id), None)
    course = next((c for c in courses if c.course_code == course_code), None)
    if student and course:
        student.enroll_course(course.course_name)
        course.add_student(student)
    else:
        print("Student or course not found.")

def add_grade():
    student_id = input("Enter Student ID: ")
    course_code = input("Enter Course Code: ")
    grade = input("Enter Grade: ")
    student = next((s for s in students if s.student_id == student_id), None)
    if student and course_code in [c.course_code for c in courses]:
        student.add_grade(course_code, grade)
    else:
        print("Student or course not found.")

def display_student_details():
    student_id = input("Enter Student ID: ")
    student = next((s for s in students if s.student_id == student_id), None)
    if student:
        student.display_student_info()
    else:
        print("Student not found.")

def display_course_details():
    course_code = input("Enter Course Code: ")
    course = next((c for c in courses if c.course_code == course_code), None)
    if course:
        course.display_course_info()
    else:
        print("Course not found.")

def main_menu():
    while True:
        print("==== Student Management System ====")
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
        
        try:
            if choice == "1":
                add_student()
            elif choice == "2":
                add_course()
            elif choice == "3":
                enroll_student_in_course()
            elif choice == "4":
                add_grade()
            elif choice == "5":
                display_student_details()
            elif choice == "6":
                display_course_details()
            elif choice == "7":
                save_data(students, courses)
            elif choice == "8":
                data = load_data()
            elif choice == "0":
                print("Exiting Student Management System. Goodbye!")
                break
            else:
                print("Invalid option.")
        except Exception as e:
            print(f"Error occurred: {e}")

# Run the main menu
if __name__ == "__main__":
    main_menu()