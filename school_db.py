from enum import Enum
import mysql.connector
from datetime import timedelta

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

    Example:

    >>> import school_db as db
    >>> db.record_new_student("maria", "metakitrina", "1900-10-05", "A")
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


def get_all_teachers():
    sql = "select * from teacher"
    my_cursor.execute(sql)
    all_teachers_list = []
    for teacher in my_cursor.fetchall():
        teacher_dictionary = {"id": teacher[0],
                              "first_name": teacher[1],
                              "last_name": teacher[2]
                              }
        all_teachers_list.append(teacher_dictionary)
    return all_teachers_list


def get_timetable_entries_for_teacher(teacher_id):
    sql = "select * from timetable_entry where teacher_id = %s"
    val = (teacher_id, )
    my_cursor.execute(sql, val)
    timetable_list = []
    for timetable_entry in my_cursor.fetchall():
        timetable_dictionary = {"day": timetable_entry[0],
                                "start": timetable_entry[1],
                                "end": timetable_entry[2],
                                "room": timetable_entry[3],
                                "subject": timetable_entry[4],
                                "teacher_id": timetable_entry[5]}
        timetable_list.append(timetable_dictionary)
    return timetable_list


def get_hours_for_teacher(teacher_id):
    timetable_list = get_timetable_entries_for_teacher(teacher_id)
    total_duration = timedelta(seconds=0)
    for timetable_entry in timetable_list:
        duration = timetable_entry["end"] - timetable_entry["start"]
        total_duration += duration
    return total_duration


def get_all_teachers_hours():
    all_teachers_hours_list = []
    for teacher in get_all_teachers():
        teacher_id = teacher["id"]
        duration = get_hours_for_teacher(teacher_id)
        teacher_dict = {"name": teacher["first_name"] + " " + teacher["last_name"],
                        "duration_minutes": duration.total_seconds()/60}
        all_teachers_hours_list.append(teacher_dict)
    return all_teachers_hours_list
