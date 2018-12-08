from flask import Flask
import json

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/yeet")
def yeet():
    return json.dumps({"good_word": "to HELL with georgia!"})


if __name__ == '__main__':
    app.run(debug=True)
