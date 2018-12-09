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


@app.route("/port", methods=["POST"])
def portQ():
    # setName = request.args.get("setName")
    # usrName = request.args.get("usrName")
    # print(usrName)
    # print(setName)
    setID = request.args.get("setID")

    worked = qh.portSet(setID)  # qh.port(usrName, setName)
    if (worked):
        return "<h3>Successfully ported set {}</h3>".format(setID)
    else:
        return "<h3>Port failed :(</h3>"


if __name__ == '__main__':
    app.run(debug=True)
