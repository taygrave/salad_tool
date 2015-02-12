import model
import sqlite3

def get_states():
    """Returns a list of the states from db for input to jinja list in html form"""
    query = """SELECT * FROM States"""
    model.CURSOR.execute(query)
    states = model.CURSOR.fetchall()
    state_list = []

    for row in states:
        state = model.State(row[0], row[1])
        state_list.append(state)

    return state_list

def get_seasons():
    """Returns a list of all seasons by making a set of db season types"""
    query = """SELECT * FROM Master"""
    model.CURSOR.execute(query)
    results = model.CURSOR.fetchall()
    seasons = set([])
    season_list = []

    for item in results:
        seasons.add(item[3])

    for item in seasons:
        if item[:1] == "E":
            abbrv = item[:1]+item[6:9]
        else:
            abbrv = item[:1]+item[5:8]

        season_list.append((abbrv,item))

    return season_list

state_list = get_states()
season_list = get_seasons()

