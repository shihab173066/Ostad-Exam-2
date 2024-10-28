import json  # Import JSON module for saving/loading data

# Define the Person class to hold basic person information
class Person:
    # code

# Define Student class inheriting from Person
class Student(Person):
    # code

# Define Course class to manage course information
class Course:
    # code

# Define StudentManagementSystem class to handle system operations
class StudentManagementSystem:
    # code

    def load_data(self, filename="data.json"):  # Load data from file
        # code

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
