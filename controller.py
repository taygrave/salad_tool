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

def season_name(seas_abbrv):
    """Queries the database based on season abbreviation (string) and returns the full name of the season (string)."""
    s = model.connect()
    season = s.query(model.Season).filter_by(abbrv=seas_abbrv).one().name
    return season

def get_N_or_S(state, seas_abbrv, ftype):
    """Queries the database based on state and season for the particular food type (Vegetable, Fruit, Seafood, or Nuts) and, if defined, number of those items (default 1). """
    s = model.connect()
    season = season_name(seas_abbrv)
    N_or_S = s.query(model.Food).filter(model.Food.state==state, model.Food.season==season, model.Food.sort==ftype).first()

    return (season, N_or_S)

def picker(state, seas_abbrv, ftype):
    """Queries the database based on state and season for the particular food type (Vegetable, Fruit, Seafood, or Nuts) and, if defined, number of those items (default 1). """
    s = model.connect()
    season = season_name(seas_abbrv)
    food_list = s.query(model.Food).filter(model.Food.state==state, model.Food.season==season, model.Food.sort==ftype).all()

    return food_list


