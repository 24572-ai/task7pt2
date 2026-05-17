# Docstring : fighter jet database created by daniel gasson


import sqlite3
#constants and variables
DATABASE = "fighters.db"

#functions
def print_all_aircraft():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "select * from fighters;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print (results)
    db.close()


#main code
print_all_aircraft()
