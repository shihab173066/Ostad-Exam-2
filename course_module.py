class Course:
    def __init__(self, course_name, course_code, instructor):
        self.course_name = course_name          # Name of the course
        self.course_code = course_code          # Unique course code
        self.instructor = instructor            # Name of the instructor
        self.students = []                      # List of students enrolled

    def add_student(self, student):
        # Add student to course if not already enrolled
        if student not in self.students:
            self.students.append(student)
            print(f"Student {student.name} added to {self.course_name}")

    def display_course_info(self):
        # Display course information
        print(f"Course Name: {self.course_name}, Code: {self.course_code}, Instructor: {self.instructor}")
        print("Enrolled Students:", ", ".join([student.name for student in self.students]))
