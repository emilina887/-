import sqlite3

connection = sqlite3.connect('student_db.sl3', 5)

cur = connection.cursor()
#cur.execute("CREATE TABLE first group (last name TEXT, first name TEXT, age INTEGER);")
cur.execute('INSERT INTO first group (last name, first name, age) VALUES ("Ivanov", "Ivan", 28);')
cur.execute('INSERT INTO first group (last name, first name, age) VALUES ("Petrov", "Sergiy", 18);')

connection.commit()
cur.execute('SELECT rowid, last_name, first name, age FROM first group')