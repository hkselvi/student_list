student_list = []

# Function definition for adding a new student
def add_student():
    name = input("Please enter the student's first name: ")
    surname = input("Please enter the student's surname: ")
    department = input("Please enter the student's department: ")
    number = input("Please enter the student's number: ")

    student_list.append({
        "name": name,
        "surname": surname,
        "department": department,
        "number": number
    })
    print("Student added successfully!!!")

# Deleting a student by its name
def delete_student_by_name():
    name = input("Please enter the first name of the student you want to delete: ")
    found_students = [student for student in student_list if student['name'].lower() == name.lower()]

    if found_students:
        print(f"Found {len(found_students)} student(s) with the name '{name}':")
        for i, student in enumerate(found_students):
            print(f"{i + 1}. {student['name']} {student['surname']}, Department: {student['department']}, Number: {student['number']}")

        try:
            choice = int(input("Please enter the roll number of the student you want to delete: ")) - 1
            selected_student = found_students[choice]
            student_list.remove(selected_student)
            print("Student deleted completely!!!")
        except (ValueError, IndexError):
            print("Invalid choice!")
    else:
        print(f"There is no student found with the name '{name}'!")


# Editing a student by its name
def edit_student_by_name():
    name = input("Please enter the first name of the student you want to edit: ")
    found_students = [student for student in student_list if student['name'].lower() == name.lower()]

    if found_students:
        print(f"Found {len(found_students)} student(s) with the name '{name}':")
        for i, student in enumerate(found_students):
            print(f"{i + 1}. {student['name']} {student['surname']}, Department: {student['department']}, Number: {student['number']}")

        try:
            choice = int(input("Please enter the number of the student you want to edit: ")) - 1
            selected_student = found_students[choice]
            index = student_list.index(selected_student)

            student_list[index]['name'] = input("Enter the new first name: ") or student_list[index]['name']
            student_list[index]['surname'] = input("Enter the new surname: ") or student_list[index]['surname']
            student_list[index]['department'] = input("Enter the new department: ") or student_list[index]['department']
            student_list[index]['number'] = input("Enter the new number: ") or student_list[index]['number']

            print("Student updated successfully!!!")
        except (ValueError, IndexError):
            print("Invalid choice!")
    else:
        print(f"There is no student found with the name '{name}'!")


# Showing the list of all students
def show_students():
    if not student_list:
        print("No students in the list.")
    else:
        print("Student List:")
        for i, student in enumerate(student_list):
            print(f"{i + 1}. {student['name']} {student['surname']}, Department: {student['department']}, Number: {student['number']}")


menu = """
1- Add a student in the list
2- Delete a student from the list by the student's name
3- Edit a selected student information
4- Show the list of students
5- Exit the program
"""

while True:
    choice = int(input("Choose one from the choices:"))
    if choice == 1:
        add_student()
    elif choice == 2:
        delete_student_by_name()
    elif choice == 3:
        edit_student_by_name()
    elif choice == 4:
        show_students()
    elif choice == 5:
        print("exiting...")
        break
    else:
        print("You did wrong choose!")
