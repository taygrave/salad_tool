import sqlite3

sfile = open("db.txt")

#process the file and build the necessary dictionaries

#searching: I live in X state, the time frame is X, I want X# of X types of food. 

def add_to_db(sfile):
    """Adds new data file to database in the Master table"""
    #making connection with SQL database
    conn = sqlite3.connect("saladtool.db")
    cursor = conn.cursor()
    query = """INSERT INTO Master (name, type, season, state) VALUES (?,?,?,?)"""

    #data file must be text with four columns, for name, type, season, and state
    for line in sfile:
        my_list = line.strip().split(",")
        vname, vtype, vseason, vstate  = my_list
        #FIXME - names cutting off at 10 chars
        cursor.execute(query, (vname, vtype, vseason, vstate))
        conn.commit()

    print "Successfully added %s to Master table in saladtool.db" %sfile


# NEXT STEPS:
# play with bootstrap to get a prettier page
# Put a list of states and their abbreviations into db
# put a list of seasons and their abbreviations into db
# use jinja to fill them into the form as options
# scrape rest of website to get complete listing of states and foods
# enter those into master table in db too