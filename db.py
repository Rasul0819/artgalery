import sqlite3
db = sqlite3.connect('database.db')
cursor = db.cursor()
cursor.execute('''
	CREATE TABLE IF NOT EXISTS artists(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT ,
		address TEXT,
		town TEXT ,
		country TEXT,
		post_code  INTEGER
		)
	''')

def add_datas_to_artists(ati,adresi,qalasi,watani,postcode):
	cursor.execute('''
		INSERT INTO artists(
			name,address,town,country,post_code)
		VALUES(?,?,?,?,?)
		''',(ati,adresi,qalasi,watani,postcode))
	db.commit()



#add_datas('Timati','Oraq balga','Nukus','Qalaraqalpaqtsan',100200)

cursor.execute('''
	CREATE TABLE IF NOT EXISTS arts(
		id INTEGER AUTO INCREMENT,
		artist_id INTEGER,
		title  TEXT,
		style TEXT,
		price INTEGER
		)

	''')

def add_datas_to_arts(artist_id,title,style,price):
	cursor.execute('''
		INSERT INTO arts(
			artist_id,title,style,price)
			VALUES(?,?,?,?)

		''',(artist_id,title,style,price))
	db.commit()


def view_all_artists():
	cursor.execute('SELECT name FROM artists')
	names = cursor.fetchall()
	list_names = []
	for i in names:
		list_names.append(i[0])
	return list_names

def view_all_arts():
	cursor.execute('SELECT title FROM arts')
	titles = cursor.fetchall()
	list_titles = []
	for i in titles:
		list_titles.append(i[0])
	return list_titles
