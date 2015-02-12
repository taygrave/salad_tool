from flask import Flask, render_template, request
from flask import session as flask_session
import controller

app = Flask(__name__)


@app.route("/", methods =["GET"])
def homepage():
    state_list = controller.state_list
    season_list = controller.season_list

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




    return render_template("base.html", state_list = state_list, season_list = season_list, state = state, season = season, veggie = veggie, vegqty = vegqty, fruit = fruit, frtqty = frtqty, nuts = nuts, seafood = seafood)




if __name__ == "__main__":
    app.run(debug = True)




# NEXT STEPS:

# form validation?
# change db so it's using sql alchemy with classes for each food type so is easier to query for
# make form submission return options from db
# scrape rest of website to get complete listing of states and foods
# enter those into master table in db too (with foreign key refs)
# play with bootstrap to get a prettier page
