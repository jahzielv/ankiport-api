from flask import Flask
from flask import request
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


@app.route('/query-example', methods=['POST'])
def query_example():
    # if key doesn't exist, returns None
    language = request.args.get('language')

    return '''<h1>The language value is: {}</h1>'''.format(language)


if __name__ == '__main__':
    app.run(debug=True)
