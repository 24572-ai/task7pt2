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
    print ('Name               speed    max_g    climb    range    payload')
    for fighter in results:
        print (f'{fighter[1]:<20}{fighter[2]:<10}{fighter[3]:<8}{fighter[4]:<8}{fighter[5]:<10}{fighter[6]:<10}')
    #loop ends
    db.close()


#main code
print_all_aircraft()
