# Docstring : fighter jet database created by daniel gasson


import sqlite3
#constants and variables
DATABASE = "fighters.db"

#functions
def print_all_aircraft():
    '''print all aircraft nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "select * from fighters;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all results
    for fighter in results:
        print (fighter)
    #loop ends
    db.close()


#main code
print_all_aircraft()
