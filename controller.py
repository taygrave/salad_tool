import model

def get_states():
    """Returns a list of the states from db for jinja input to formselect"""
    #FIXME: Have return only states that have food info in Foods table
    s = model.connect()
    allstates = s.query(model.State).all()
    state_list = []

    for state in allstates:
        state_list.append((state.abbrv, state.name))

    return state_list

def get_seasons():
    """Returns a list of all seasons from db for jinja input to formselect"""
    s = model.connect()
    allseasons = s.query(model.Season).all()
    season_list = []

    for season in allseasons:
        season_list.append((season.abbrv,season.name))

    return season_list

def pickme(state, season, ftype, number=1):
    """Queries the database based on state and season for the particular food type (Vegetable, Fruit, Seafood, or Nuts) and, if defined, number of those items (default 1). """
    pass



