from flask import Flask, render_template, request

from challenges.evaluate_code import evaluate

import os
import yaml

app = Flask(__name__)


def fetch_questions():
    dirs = os.listdir("challenges/")
    db = {}
    for dir in dirs:
        if os.path.isdir("challenges/" + dir) and dir != "__pycache__":
            with open("challenges/" + dir + "/config.yaml", "r") as config_file:
                contents = yaml.load(config_file, Loader=yaml.FullLoader)
            db[dir] = contents

    return db


database = fetch_questions()


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", database=database)


@app.route("/<location>", methods=["POST", "GET"])
def question(location):
    boiler_plate_code = open("challenges/" + location + "/code.py", "r").readlines()
    message = ""
    if request.method == "POST":
        if request.form.get("submit__code__button") == "Submit":
            output = request.form.to_dict()
            code = output["code"]
            state = evaluate(location, database[location], code)

            return render_template(
                "question.html",
                location=location,
                contents=database[location],
                message=state["message"],
                success=state["success"],
                textarea_value=code
            )

    return render_template(
        "question.html", location=location, contents=database[location], textarea_value=boiler_plate_code
    )

"""
@app.route("/questions")
def questions():
    return render_template("questions.html", database=database)
"""
if __name__ == "__main__":
    app.run(debug=True, port=5001)
