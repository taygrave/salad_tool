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



    return render_template("base.html", state_list = state_list, season_list = season_list, state = state, season = season)

@app.route("/made", methods =["GET"])
def make_salad():
    state = request.args.get("state")
    season = request.args.get("season")

    return render_template("SaladHome.html", state = state, season = season)



if __name__ == "__main__":
    app.run(debug = True)