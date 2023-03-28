from flask import Flask, render_template, request

from challenges import evaluate_code

import os
import json
import yaml

app = Flask(__name__)


def fetch_questions():
    dirs = os.listdir("challenges/")

    locations = []
    titles = []

    for dir in dirs:
        with open(dir + "config.yaml", "r") as config_file:
            contents = yaml.load(config_file, Loader=yaml.FullLoader)

        locations.append("challenges/" + dir)
        titles.append(contents["title"])

    return locations, titles


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/allquestions")
def allquestions():
    question_locations, titles = fetch_questions()
    return render_template(
        "allquestions.html", question_locations=question_locations, titles=titles
    )


@app.route("/quizzer", methods=["POST", "GET"])
def quizzer():
    message = ""
    if request.method == "POST":
        if request.form.get("submit__code__button") == "Submit code":
            output = request.form.to_dict()
            code = output["code"]
            state = evaluate_code(code) # TODO: ID is now an arg

            return render_template(
                "quizzer.html", message=state["message"], success=state["success"]
            )

    return render_template("quizzer.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
