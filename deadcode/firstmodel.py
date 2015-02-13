from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, scoped_session, relationship, backref

import sqlite3
import csv

Base = declarative_base()

ENGINE = create_engine("sqlite:///saladtool.db", echo=True)
Session = sessionmaker(bind=ENGINE)
session = Session()

#process the file and build the necessary dictionaries

#searching: I live in X state, the time frame is X, I want X# of X types of food. 

CONN = sqlite3.connect("saladtool.db")
CURSOR = CONN.cursor()

#Use this for one time adds to db of all foods once scraped new data from web: http://www.sustainabletable.org/seasonalguide/seasonalfoodguide.php
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

#Already used for a one-time add to db for list of states
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

class Food(Base):


