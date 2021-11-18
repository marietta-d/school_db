import school_db as db
import mysql.connector
import matplotlib.pyplot as plt
import numpy as np
import json

with open('private/db_password.json') as json_file:
    private_data = json.load(json_file)

my_db = mysql.connector.connect(
    host="localhost",
    user=private_data["db_username"],
    password=private_data["db_password"],
    database="school"
    )
my_cursor = my_db.cursor()

print(db.get_all_teachers_hours())
x_cache = np.empty(shape=(0,))  # empty means: []
y_cache = np.empty(shape=(0,))  # []
for teacher in db.get_all_teachers_hours():
    x_curr = teacher["name"]
    y_curr = teacher["duration_minutes"]
    # np.concatenate( TUPLE of np.arrays),
    x_cache = np.concatenate((x_cache, [x_curr]))  # [x_curr] is a list
    y_cache = np.concatenate((y_cache, [y_curr]))
plt.bar(x_cache, y_cache)
plt.xticks(x_cache, rotation ="vertical")
plt.gcf().subplots_adjust(bottom=0.35)
plt.show()
