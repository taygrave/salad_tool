from flask import Flask, render_template, request
from flask import session as flask_session
from random import choice, sample
import controller

app = Flask(__name__)


@app.route("/", methods=["GET"])
def homepage():

    state_list = controller.get_states()
    season_list = controller.get_seasons()

    #FIXME: gotta put in some form validation

    state = request.args.get("state")
    season = request.args.get("season")
    veggie = request.args.get("veggie")
    vegqty = request.args.get("vegqty")
    fruit = request.args.get("fruit")
    frtqty = request.args.get("frtqty")
    nuts = request.args.get("nuts")
    seafood = request.args.get("seafood")

    check_dict = {"Vegetable": (veggie, vegqty), "Fruit": (fruit, frtqty), "Nuts": (nuts, 1), "Seafood": (seafood, 1)}

    season = controller.season_name(season)
    
    food_choices = {}
    food_choices['messages'] = []

    for key in check_dict:
        if check_dict[key][0] == 'on':
            ftype = key
            qty = int(check_dict[key][1])

            food_list = controller.picker(state, season, ftype)

            if qty > len(food_list):
                qty = len(food_list)
                
                #TODO: Fix messages to make more linguistic sense
                if qty != 0:
                    msg = "* Only %d %s availalbe" %(qty, ftype)
                else: 
                    msg = "* %s not avaialble" %(ftype)
                
                food_choices['messages'].append(msg)

            food_choices[ftype] = sample(food_list, qty)

            #add a msg key to food_choices and print all relevant messages too?

            print food_choices


    return render_template("base.html", state_list=state_list, season_list=season_list, state=state, season=season, check_dict=check_dict, food_choices=food_choices)


if __name__ == "__main__":
    app.run(debug = True)




# NEXT STEPS:

# form validation and values sticking after submission so you can see what you queried
# change qty buttons to radio buttons for 1-5??
# reset button to allow individual re-queries for disliked result foods w/o restting whole thing
# play with bootstrap to get a prettier page
# scrape rest of website to get complete listing of states and foods
# enter those into master table in db too (with foreign key refs)
# add options for 'always available' items, dried fruits, crunchies, cheese, canned beans / chickpeas, other things
