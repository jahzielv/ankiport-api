from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/yeet")
def yeet():
    return "yeet"


if __name__ == '__main__':
    app.run(debug=True)
