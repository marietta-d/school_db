import mysql.connector
my_db = mysql.connector.connect(
    host="localhost",
    user="marietta",
    password="pythonis@BIGsnAK3",
    database="school"
    )

my_cursor = my_db.cursor()


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





