from enum import Enum
import mysql.connector
my_db = mysql.connector.connect(
    host="localhost",
    user="marietta",
    password="pythonis@BIGsnAK3",
    database="school"
    )

my_cursor = my_db.cursor()


class Day(Enum):
    Monday = "Monday"
    Tuesday = "Tuesday"
    Wednesday = "Wednesday"
    Thursday = "Thursday"
    Friday = "Friday"


def record_new_student(first_name, last_name, birth_date, level="A"):
    """
    :param first_name:
    :param last_name:
    :param birth_date:
    :param level:
    :return: student's ID
    """

    sql = "insert into student (first_name, last_name, date_of_birth, level) values (%s, %s, %s, %s)"
    val = (first_name, last_name, birth_date, level)
    my_cursor.execute(sql, val)
    my_db.commit()
    return my_cursor.lastrowid


def delete_student(student_id):
    sql = "delete from student where id = %s"
    my_cursor.execute(sql, (student_id,))
    my_db.commit()


def record_new_teacher(first_name, last_name):
    sql = "insert into teacher (first_name, last_name) values (%s, %s)"
    val = (first_name, last_name)
    my_cursor.execute(sql, val)
    my_db.commit()
    return my_cursor.lastrowid


def record_new_subject(subject_name, subject_level, subject_id):
    sql = "insert into subject (name, level, id) values (%s, %s, %s)"
    val = (subject_name, subject_level, subject_id)
    try:
        my_cursor.execute(sql, val)  # may raise Exception if pr. key exists
        my_db.commit()
        return my_cursor.lastrowid
    except mysql.connector.errors.IntegrityError:
        return None


def record_new_timetable_entry(day, start_time, end_time, room, subject_id, teacher_id):
    assert(type(day) == Day)
    sql = "insert into timetable_entry (day, start, end, room, subject_id, teacher_id) values (%s, %s, %s, %s, %s, %s)"
    val = (day.value, start_time, end_time, room, subject_id, teacher_id)
    my_cursor.execute(sql, val)
    my_db.commit()


def new_registration(student_id, subject_id):
    sql = "insert into registrations (student_id, subject_id) values (%s, %s)"
    val = (student_id, subject_id)
    my_cursor.execute(sql, val)
    my_db.commit()


def new_teaching_capability(teacher_id, subject_id):
    """
    Teaching capability means that Teacher X can teach Subject Y.
    """
    sql = "insert into teacher_subject (teacher_id, subject_id) values (%s, %s)"
    val = (teacher_id, subject_id)
    my_cursor.execute(sql, val)
    my_db.commit()

# def find_teacher_for_subject_name():
