import sqlite3

db = sqlite3.connect("fighters.db")
cursor = db.cursor()
sql = "select * from fighters;"
cursor.execute(sql)
results = cursor.fetchall()
print (results)
db.close()
