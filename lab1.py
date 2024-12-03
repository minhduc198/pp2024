
students = []
def addStudent():
    num = int(input("Enter the number stu: "))

    for i in range (num):
       Id = input("enter id: ")
       name = str(input("enter full name: "))
       DoB = input("enter doB: ")

       print("-------------------")

       student = {
        "id": Id,
        "name": name,
        "Dob": DoB
       }

       students.append(student)

    task()

# # courses
courses = []
def addCourse(): 
    numCourses = int(input("Enter the number courses: "))
    for i in range (numCourses):
       Id = input("enter id: ")
       name = str(input("enter name course: "))

       print("-------------------")

       course = {
        "id": Id,
        "name": name
       }

       courses.append(course)

    task()

def disPlayCourses(courses):

    if (len(courses) <= 0): print("---------Nothing") 

    for course in courses:
        print(f'ID: {course['id']},  Name: {course['name']}')
    print("--------------------")
    
    task()

def inputMark(students, courses): 


    if (len(courses) <= 0): 
        print("----------does not has courses")
        return task()
    
    if (len(students) <= 0): 
        print("------------does not has student")
        return task()

    Id = int(input("Enter id for mark: "))



    score = {}
    for course in courses: 
        mark = (input("input the mark of " + course['name'] + ": "))
        mark = {
            course["name"]: (mark)
        }
        
        score.update(mark)

    for student in students: 
        if (int(student['id']) == Id):
            student.update(score)
            return task()
        else: 
            print("does not exit this student")
            return task()

def disPlayScore(students, courses):
    if (len(students) <= 0): print("---------Nothing") 

    for student in students:
        subjects = []
        for course in courses:
          value = student.get(course['name'], "empty") 
          subjects.append(f"{course['name']}: {value}")

          subjectsToStr = " - ".join(subjects)

        print(f"ID: {student['id']}, Name: {student['name']}, Courses: {subjectsToStr}")

    print("--------------------")
    
    task()

def removeStu(students): 

    id = int(input("Id to remove: "))
    # [students.remove(student) for student in students if int(student['id']) == id]
    for student in students:
        if(int(student['id']) == id): students.remove(student)
        else: 
            print("-------does not have id in list")
            return task()
    print("------------completed")

    task()

def disPlayStu(students):

    if (len(students) <= 0): print("---------Nothing") 

    for student in students:
        print(f'ID: {student['id']},  Name: {student['name']},  Dob: {student['Dob']}')
    print("-----------------")
    
    task()

def todo(num):
    if (num == 0): return
    elif  (num == 1): addStudent()
    elif  (num == 2): removeStu(students)
    elif  (num == 3): disPlayStu(students)
    elif  (num == 4): addCourse()
    elif  (num == 5): disPlayCourses(courses)
    elif  (num == 6): inputMark(students, courses)
    elif  (num == 7): disPlayScore(students, courses)
    else: 
        print("try again")
        return task()

def task():
    print("0. exist") 
    print("1. add student") 
    print("2. kick student") 
    print("3. display student")
    print("4. add courses")
    print("5. disPlay courses")
    print("6. input score")
    print("7. display score")

    chose = int(input("chose: "))
    todo(chose)
task()


    



