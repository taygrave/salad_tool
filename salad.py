from flask import Flask, render_template
from flask import session as flask_session
import model

app = Flask(__name__)


@app.route("/")
def homepage():
    state_list = model.state_list
    return render_template("base.html", state_list = state_list)

if __name__ == "__main__":
    app.run(debug = True)