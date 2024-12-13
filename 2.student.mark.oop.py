class Person:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob

    def display(self):
        return f"ID: {self.id}, Name: {self.name}, DOB: {self.dob}"


class Student(Person):
    def __init__(self, id, name, dob):
        super().__init__(id, name, dob)
        self.scores = {}

    def add_score(self, course_name, mark):
        self.scores[course_name] = mark

    def display_scores(self, courses):
        subjects = [f"{course.name}: {self.scores.get(course.name, 'empty')}" for course in courses]
        return f"{self.display()}, Courses: {', '.join(subjects)}"


class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def display(self):
        return f"ID: {self.id}, Name: {self.name}"


class Run:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self):
        num = int(input("Enter the number of students: "))
        for _ in range(num):
            id = input("Enter student ID: ")
            name = input("Enter full name: ")
            dob = input("Enter DOB: ")
            self.students.append(Student(id, name, dob))
        print("Students added\n")

    def display_students(self):
        if not self.students:
            print("No students")
        else:
            for student in self.students:
                print(student.disPlay())
        print("-----------------")

    def remove_student(self):
        id = input("Enter the student id to remove: ")
        for student in self.students:
            if student.id == id:
                self.students.remove(student)
                print("Student removed\n")
                return
        print("Cannot find student\n")

    def add_course(self):
        num = int(input("Enter the number of courses: "))
        for null in range(num):
            id = input("Enter course id: ")
            name = input("Enter course name: ")
            self.courses.append(Course(id, name))
        print("Courses added")

    def display_courses(self):
        if not self.courses:
            print("No courses")
        else:
            for course in self.courses:
                print(course.display())
        print("-----------------")

    def input_marks(self):
        if not self.students:
            print("No students")
            return
        if not self.courses:
            print("No courses")
            return

        student_id = input("Enter the student id to input marks: ")
        student = next((s for s in self.students if s.id == student_id), None)
        if not student:
            print("Does not find student\n")
            return

        for course in self.courses:
            mark = input(f"Enter mark for {course.name}: ")
            student.add_score(course.name, mark)
        print("Done\n")

    def display_scores(self):
        if not self.students:
            print("No students")
            return

        for student in self.students:
            print(student.display_scores(self.courses))
        print("-----------------")

    def task(self):
        while True:
            print("0. Exit")
            print("1. Add student")
            print("2. Remove student")
            print("3. Display students")
            print("4. Add course")
            print("5. Display courses")
            print("6. Input marks")
            print("7. Display scores")

            choice = int(input("Choose an option: "))

            if choice == 0:
                break
            elif choice == 1:
                self.add_student()
            elif choice == 2:
                self.remove_student()
            elif choice == 3:
                self.display_students()
            elif choice == 4:
                self.add_course()
            elif choice == 5:
                self.display_courses()
            elif choice == 6:
                self.input_marks()
            elif choice == 7:
                self.display_scores()
            else:
                print("try again: ")

if __name__ == "__main__":
    system = Run().task()
