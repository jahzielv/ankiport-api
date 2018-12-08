from flask import Flask
import json
import ankiport_core.quizlet_helper as qh

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/yeet")
def yeet():
    return json.dumps({"good_word": "to HELL with georgia!"})


@app.route("/test")
def test():
    return qh.apiTest("hello ")


if __name__ == '__main__':
    app.run(debug=True)
