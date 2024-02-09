import sqlite3


db = sqlite3.connect('database.db')
cursor = db.cursor()
cursor.execute('''
	SELECT name FROM artists''')

name = cursor.fetchall()

print(name)
for i in name:
	if i[0] == 'Timati':
		print(i[0])