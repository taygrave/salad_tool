from flask import Flask, render_template, request
from flask import session as flask_session
from random import choice, sample
import controller

app = Flask(__name__)


@app.route("/", methods=["GET"])
def homepage():

    state_list = controller.get_states()
    season_list = controller.get_seasons()

    state = request.args.get("state")
    season = request.args.get("season")
    veggie = request.args.get("veggie")
    vegqty = request.args.get("vegqty")
    fruit = request.args.get("fruit")
    frtqty = request.args.get("frtqty")
    nuts = request.args.get("nuts")
    seafood = request.args.get("seafood")

    # some formulas here for querrying db from controller file depending on form inputs

    # if veggie is 'on' then search db for veggies from selected state and season only and return vegqty # of items
    # same for fruit (could even be done in same formula)
    # if nuts, seafood on return one (maybe even these in the same formula with the # of things being a default!)
    #controller.pickme(state, season, ftype, [#])

    check_dict = {"veggie": (veggie, vegqty), "fruit": (fruit, frtqty), "nuts": (nuts, 1), "seafood": (seafood, 1)}

    # def pickme(state, seas_abbrv, ftype, number=1)
    
    # if check_dict['nuts'][0] == 'on':
    #     season, nut = controller.get_N_or_S(state, season, "Nuts", 1)
    #     if nut != None:
    #         nut = nut.name
    #     else:
    #         nut = "No local nuts available in %s." %season
    #     print nut

    # if check_dict['seafood'][0] == 'on':
    #     season, seafood = controller.get_N_or_S(state, season, "Seafood", 1)
    #     if seafood != None:
    #         seafood = seafood.name
    #     else:
    #         seafood = "No local seafood available in %s." %season
    #     print seafood

    if check_dict['veggie'][0] == 'on':
        ftype = "Vegetable"
        qty = int(check_dict['veggie'][1])

        veg_list = controller.picker(state, season, ftype)
        veg_choices = sample(veg_list, qty) 

        print veg_choices
        



    return render_template("base.html", state_list=state_list, season_list=season_list, state=state, season=season, check_dict=check_dict, veg_choices=veg_choices)




if __name__ == "__main__":
    app.run(debug = True)




# NEXT STEPS:

# form validation?
# change db so it's using sql alchemy with classes for each food type so is easier to query for
# make form submission return options from db
# scrape rest of website to get complete listing of states and foods
# enter those into master table in db too (with foreign key refs)
# play with bootstrap to get a prettier page
