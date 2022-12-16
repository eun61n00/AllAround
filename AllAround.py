import pymysql


def register_student_info():

    conn = pymysql.connect(
        user='root',
        passwd='P@ssw0rd',
        host='127.0.0.1',
        db='allaround',
        charset='utf8'
    )

    cursor = conn.cursor()

    print("========== Register Student Info ==========")

    print("Enter your information\nStudent Id: ", end="")
    id = input()

    print("Name: ", end="")
    name = input()

    print("Department: ", end="")
    department = int(input())

    query = f"INSERT INTO student (student_id, department, name) VALUES (\"{id}\", {department}, \"{name}\")"
    print(query)
    cursor.execute(query)
    conn.commit


def enroll_lecture():
    print("========== Enroll Lecture for Student ==========")

    print("Enter your student id: ", end="")
    student_id = input()

    print("Enter lecture id you enrolled in: ", end="")
    lecture_id = input()

    # insert_enrolled_lecture(student_id, lecture_id)
    query = "UPDATE student SET lecture = %d WHERE student_id = %d"
    value = (lecture_id, student_id)

    cursor.execute(query, value)


def register_event():
    print("========== Register Event ==========")


def select_option():
    print("\n\n========= Select option ==========")
    print("1. Register Student Info")
    print("2. Enroll Lecture")
    print("3. Register Event")
    print("0. Exit")
    user_selection_option = int(input())

    if user_selection_option == 0:
        exit()
    elif user_selection_option == 1:
        register_student_info()
    elif user_selection_option == 2:
        enroll_lecture()
    elif user_selection_option == 3:
        register_event()
    else:
        "Please enter right option number"


if __name__ == "__main__":

    host = "127.0.0.1"
    port = 3306
    database = "allaround"
    username = "root"
    password = "P@ssw0rd"

    conn = pymysql.connect(
        user='root',
        passwd='P@ssw0rd',
        host='127.0.0.1',
        db='allaround',
        charset='utf8'
    )

    cursor = conn.cursor()
    print("connect database successfully")

    while (True):

        select_option()
        cursor = conn.cursor()
