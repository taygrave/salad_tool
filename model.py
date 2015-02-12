import sqlite3
import csv

#process the file and build the necessary dictionaries

#searching: I live in X state, the time frame is X, I want X# of X types of food. 

CONN = sqlite3.connect("saladtool.db")
CURSOR = CONN.cursor()

def add_to_db(sfile):
    """Adds new data file to database in the Master table"""

    #sfile = "db.txt" for current data 

    #making connection with SQL database
    query = """INSERT INTO Master (name, type, season, state) VALUES (?,?,?,?)"""

    #data file must be text with four columns, for name, type, season, and state
    for line in sfile:
        my_list = line.strip().split(",")
        vname, vtype, vseason, vstate  = my_list
        CURSOR.execute(query, (vname, vtype, vseason, vstate))
        CONN.commit()

    print "Successfully added %s to Master table in saladtool.db" %sfile

def states_to_db():
    """Adds new data file to database in the States table"""
    #making connection with SQL database
    query = """INSERT INTO States (abbrv, state) VALUES (?,?)"""

    with open("states.csv", 'rb') as src_file:
        reader = csv.reader(src_file)

        for line in reader:
            state, abbrv  = line
            CURSOR.execute(query, (abbrv, state))
            CONN.commit()

    print "Successfully added states to States table in saladtool.db"

#Q: Did i really have to create a class? cant I return these values better?? Was getting an error if i just returned the result of the following function w/o making a whole class and everything
class State(object):
    """A wrapper that corresponds to rows in the States table"""
    def __init__(self, abbrv, state):
        self.abbrv = abbrv
        self.state = state

    def __repr__(self):
        return "<State: %s, %s>" %(self.abbrv, self.state)


def get_states():
    """Returns a list of the states from db for input to jinja list in html form"""
    query = """SELECT * FROM States"""
    CURSOR.execute(query)
    states = CURSOR.fetchall()
    state_list = []

    for row in states:
        state = State(row[0], row[1])
        state_list.append(state)

    return state_list

state_list = get_states()



# NEXT STEPS:

# Put a list of states and their abbreviations into db
# put a list of seasons and their abbreviations into db
# use jinja to fill them into the form as options
# scrape rest of website to get complete listing of states and foods
# enter those into master table in db too
# play with bootstrap to get a prettier page


