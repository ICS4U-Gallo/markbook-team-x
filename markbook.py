"""
Markbook Application
Group members: Lucas, Richard, Alex Lee, Joe, Matthew
"""




from typing import Dict
import json

data = {}
data['student_list'] = []
data['student_data'] = {}
data['assignment_list'] = []
data['classroom_list'] = []
data['classroom_data'] = {}


def create_assignment(name: str, due: str, points: int, classcode: str) -> Dict:
    """Creates an assignment represented as a dictionary

    Args:
        name: the name of the assignment.
        due: the due date for the assignment.
        points: what the assignment is out of (denominator).
    Returns:
        Assignment as a dictionary.
    """
    return {"name": name,
            "due": due,
            "points": points,
            "classcode": classcode}


def create_classroom(course_code: str, course_name: str, period: int, teacher: str) -> Dict:
    """Creates a classroom dictionary"""
    return {"CourseCode": course_code, "CourseName": course_name, "Period": period,
    "Teacher": teacher, "Students": []}


def add_student_to_classroom(first_name: str, last_name: str, course_code: str):
    """Adds student to a classroom
    Args:
        student: Student dict
        classroom: The classroom to add the stu to
    """
    student_name = first_name + ' ' + last_name
    with open('data.txt') as json_file:
        data = json.load(json_file)
        for classroom in data["classroom_list"]:
            if course_code == classroom["CourseCode"]:
                classroom["Students"].append(student_name)
                print("Student added to classroom.")
                with open('data.txt', 'w') as outfile:
                    json.dump(data, outfile)
            else:
                print("That is not an eligible class code or the class doesn't exist.")

    pass

#adds a student to the database
def create_student(first_name: str, last_name: str, gender: str, student_number: int, grade: int, email: str, mark: int) -> Dict:
    return {"first_name": first_name, "last_name": last_name,
            "gender": gender, "student_number": student_number, "grade": grade, "email": email}

#removes a student from the database
def remove_student_from_classroom(first_name: str, last_name: str, course_code: str):
    student_name = first_name + ' ' + last_name
    with open('data.txt') as json_file:
        data = json.load(json_file)
        for classroom in data["classroom_list"]:
            if course_code == classroom["CourseCode"]:
                classroom["Students"].remove(student_name)
                print("Student removed from classroom.")
                with open('data.txt', 'w') as outfile:
                    json.dump(data, outfile)
            else:
                print("That is not an eligible class code or the class doesn't exist.")

    pass

#edits a student
def edit_student(key, value):
    """Edits the student's info with the provided key/value pairs
    Args:
        student: The student whose data needs to be udated.
        **kwargs: KeyWordARGumentS. The key/value pairs of the
            data that needs to be changed. Can come in the form
            of a dictionary.
    """
    with open('data.txt') as json_file:
        data = json.load(json_file)
        for student in data["student_list"]:
            student[key] = value
            with open('data.txt', 'w') as outfile:
                json.dump(data, outfile)
    pass

#main menu, uses numbers as commands
print("Markbook v.1002323020302")
print("In the markbook program we use numbers as commmands, below are the following numbers which will allow for you to navigate the database. \n")
while True:
    try:
        command = int(input(" 1 -- allows for the creation of data \n 2 -- Shows you the current data within the system \n 3 -- allows you to remove/edit data \n 4 -- Save all and exit. \n"))
    except:
        print("That is not a command, please see help for more details.")
    else:
        if command not in range(1, 5):
            print("That is not a command, please see help for more details.")
        elif command == 1:
            while True:
                try:
                    num = int(input(" 1 -- Create a student profile \n 2 -- Create an assignment \n 3 -- Create a classroom \n 4 -- Back \n"))
                except:
                    print("That is not a selectable number.")
                else:
                    if num not in range(1, 5):
                        print("please pick a number between 1 or 4.")
                    elif num == 1:
                        first_name = str(input("First Name:"))
                        last_name = str(input("Last Name:"))
                        gender = str(input("Gender:"))
                        student_number = int(input("Student Number:"))
                        grade = int(input("Grade (number):"))
                        email = str(input("Email:"))

                        data['student_list'].append(create_student(first_name, last_name, gender, student_number, grade, email))

                        with open('data.txt', 'w') as outfile:
                            json.dump(data, outfile)

                        print("Student Inputted.")

                    elif num == 2:
                        name = str(input("Name of Assignment:"))
                        due = str(input("Due Date:"))
                        points = int(input("Marks the assignment is out of:"))
                        coursecode = str(input("Course Code of the class the assignment is being added to:"))

                        data['assignment_list'].append(create_assignment(name, due, points, coursecode))
                        with open('data.txt', 'w') as outfile:
                            json.dump(data, outfile)

                        print("Assignment Inputted.")

                    elif num == 3:
                        course_code = str(input("Course Code:"))
                        course_name = str(input("Course Name:"))
                        period = int(input("Period (number):"))
                        teacher = str(input("Teacher:"))

                        data['classroom_list'].append(create_classroom(course_code, course_name, period, teacher))
                        with open('data.txt', 'w') as outfile:
                            json.dump(data, outfile)

                        print('Classroom inputted.')

                    elif num == 4:
                        break

        elif command == 2:
            while True:
                try:
                    num = int(input(" 1 -- preview student list \n 2 -- preview classroom list \n 3 -- View current assignments created \n"))
                except:
                    print("That is not an eligible number.")
                else:
                    if num not in range(1, 5):
                        print("please pick a number between 1 to 4.")
                    elif num == 1:
                        with open('data.txt') as json_file:
                            data = json.load(json_file)
                            for student in data["student_list"]:
                                for key, value in student.items():
                                    print(key, "|", value)
                                    print("---------------------")
                    elif num == 2:
                        with open('data.txt') as json_file:
                            data = json.load(json_file)
                            for classroom in data["classroom_list"]:
                                for key, value in classroom.items():
                                    print(key, "|", value)
                                    print("---------------------")

                    elif num == 3:
                        with open('data.txt') as json_file:
                            data = json.load(json_file)
                            for assignment in data["assignment_list"]:
                                for key, value in assignment.items():
                                    print(key, "|", value)
                                    print("----------------------")


                    elif num == 4:
                        break

        elif command == 3:
            while True:
                try:
                    num = int(input(" 1 -- add a student to a classroom \n 2 -- remove a student from a classroom \n 3 -- edit a student's info \n 4 -- exit \n"))
                except:
                    print("That is not an eligible number.")
                else:
                    if num not in range(1, 5):
                        print("Please pick a number between 1 to 4")
                    elif num == 1:
                        first_name = str(input("Student's first name:"))
                        last_name = str(input("Student's last name:"))
                        course_code = str(input("Course code of the class thent is to be added to:"))
                        add_student_to_classroom(first_name, last_name, course_code)

                    elif num == 2:
                        first_name = str(input("Student's first name:"))
                        last_name = str(input("Student's last name:"))
                        course_code = str(input("Course code of the class the student is to be removed from:"))
                        remove_student_from_classroom(first_name, last_name, course_code)

                    elif num == 3:
                        while True:
                            try:
                                student_number = int(input("Please input the student number:"))
                            except:
                                print("That is not a student within our database.")
                            else:
                                with open('data.txt') as json_file:
                                    data = json.load(json_file)
                                    for student in data["student_list"]:
                                        if student_number != student["student_number"]:
                                            print("That is not a student within out database.")
                                        elif student_number == student["student_number"]:
                                            while True:
                                                try:
                                                    num = int(input(" 1 -- Change the first name \n 2 -- Change the last name \n 3 -- Change the gender \n 4 -- Change the student number \n 5 -- Change the grade \n 6 -- Change the email \n 7 -- back \n"))
                                                except:
                                                    print("That is not a valid number.")
                                                else:
                                                    if num not in range(1, 8):
                                                        print("That is not a valid number.")
                                                    elif num == 1:
                                                        value = str(input("Change the student's first name:"))
                                                        key = "first_name"
                                                        edit_student(key, value)
                                                        print("Changes saved.")
                                                    elif num == 2:
                                                        value = str(input("Change the student's last name:"))
                                                        key = "last_name"
                                                        edit_student(key, value)
                                                        print("Changes saved.")
                                                    elif num == 3:
                                                        value = str(input("Change the student's gender:"))
                                                        key = "gender"
                                                        edit_student(key, value)
                                                        print("Changes saved.")
                                                    elif num == 4:
                                                        value = int(input("Change the student's number:"))
                                                        key = "student_number"
                                                        edit_student(key, value)
                                                        print("Changes saved.")
                                                    elif num == 5:
                                                        value = int(input("Change the student's grade:"))
                                                        key = "grade"
                                                        edit_student(key, value)
                                                        print("Changes saved.")
                                                    elif num == 6:
                                                        value = str(input("Change the student's email:"))
                                                        key = "email"
                                                        edit_student(key, value)
                                                        print("Changes saved.")
                                                    elif num == 7:
                                                        break
                            if num == 7:
                                break

                    elif num == 4:
                        break
                        
        elif command == 4:
            print("All changes inputted.")
            with open('data.txt', 'w') as outfile:
                json.dump(data, outfile)
            break


                                                       
                            
