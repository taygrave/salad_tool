from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, distinct
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, backref
import dictstates
import csv

Base = declarative_base()

ENGINE = None
Session = None

########################
####  INITIALIZING  ####
########################

def reset_all(dbname):
    """Starts a completely new database named as you wish. Will create all three tables for States, Seasons, and Foods"""
    database = "sqlite:///" + dbname + ".db"
    engine = create_engine(database, echo=True)
    Base.metadata.create_all(engine)

def load_all():
    """Will load all your empty tables in a brand new database, modify inner code to define starting source files for each table"""
    s = connect()
    load_foods(s, "data/starterfoods.csv")
    load_states(s)
    load_seasons(s)
    print "CONGRATULATIONS! All tables loaded."


########################
##BUILDING THE DATABASE#
########################
    # As of 2/12/15 saladmixie already created
    # To create a brand new db must run the following two lines of code outside of any function:
    # engine = create_engine("sqlite:///New_DB_name.db", echo=True)
    # Base.metadata.create_all(engine)

class State(Base):
    __tablename__ = "States"
    abbrv = Column(String(2), primary_key = True)
    name = Column(String(25), nullable = False)

    def __repr__(self):
        return "<State: abbrv=%s, name=%s>" %(self.abbrv, self.name)

class Season(Base):
    __tablename__ = "Seasons"
    name = Column(String(25), primary_key = True)
    abbrv = Column(String(4), primary_key = True)

    def __repr__(self):
        return "<Season: name=%s abbrv=%s>" %(self.name, self.abbrv)

class Food(Base):
    __tablename__ = "Foods"
    id = Column(Integer, primary_key = True)
    state = Column(String(2), ForeignKey('States.abbrv'), nullable = False)
    season = Column(String(15), ForeignKey('Seasons.name'), nullable = False)
    name = Column(String(30), nullable = False)
    sort = Column(String(15), nullable = False)

    states = relationship('State', backref=backref('foods', order_by=id))
    seasons = relationship('Season', backref=backref('foods', order_by=id))

    def __repr__(self):
        return "<Food: id=%r state=%s season=%s name=%s sort=%s>" %(self.id, self.state, self.season, self.name, self.sort)

def connect():
    """This creates a connection to the existing db, to use type session = connect() into your python console using this module"""

    global ENGINE
    global Session

    ENGINE = create_engine("sqlite:///saladmixie.db", echo=True)
    Session = sessionmaker(bind=ENGINE)

    return Session()

########################
##LOADING THE DATABASE##
########################
    # Use this for one time adds to db of all foods once scraped new data from web: http://www.sustainabletable.org/seasonalguide/seasonalfoodguide.php
    # Currently, all data files located in /data directory

def load_foods(session, src_file):
    """Adds new food data file to database in the Master table, data file must be text with four columns, 1) name, 2) type, 3) season, and 4) state"""
    with open(src_file, 'rb') as food_file:
        reader = csv.reader(food_file)

        for row in reader:
            name, sort, season, state  = row
            entry = Food(state=state, season=season, name=name, sort=sort)
            session.add(entry)

        session.commit()
    print "Successfully added %s file to Foods table in db" %src_file

def load_states(session):
    """Adds distinct states to the States table, sourcing from states which appear in current version of Foods table"""
    state_list = session.query(Food.state).distinct().all()

    for state in state_list:
        abbrv = state[0] #FIXME: Like for seasons, not sure why returns as tuple
        name = dictstates.states_dict[abbrv]
        print abbrv, type(abbrv)
        print name, type(name)
        
        entry = State(abbrv=abbrv, name=name)
        session.add(entry)

    session.commit()
    print "Successfully added states to States table to db"

def load_seasons(session):
    """Adds distinct seasons to the season table, sourcing from seasons listed in the Foods table (thus requires non-empty Seasons table)"""
    season_list = session.query(Food.season).distinct().all()

    for item in season_list:
        #FIXME for some reason the query is returning tuples, thus the [0] index distinction
        season = item[0]

        #making abbreviations depending on 'early' or 'late'
        if season[:1] == "E":
            abbrv = season[:1]+season[6:9]
        else:
            abbrv = season[:1]+season[5:8]

        entry = Season(abbrv=abbrv, name=season)
        session.add(entry)

    session.commit()
    print "Successfully updated Seasons table in db"


# To add new data to database, call one of the functions above, using after calling "s = connect()" as the session parameter for said function and type in the path of the csv data file to be imported as the second parameter
# Will not work if replacing exisiting unique primary key ids
# FIXME: Figure out or write new functions so that if new data is added to a file with existing and already loaded data, will only add new data to the db


