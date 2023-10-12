

# Given list of students
student_list = [{id: 1, "name": "rajesh"},{id: 2, "name": "rahul"},{id: 3, "name": "sruthi"}]

# Accepting input from the user
student_id = int(input("Enter the student ID: "))

def get_name_by_id(student_list, student_id):

    # Iteration for matching the id of student
    for student in student_list:
        if student[id] == student_id:
            return student['name']

# Getting the name of the student
student_name = get_name_by_id(student_list, student_id)

# Printing the result
if student_name:
    print("Student name:", student_name)
else:
    print("Student not found with ID:", student_id)