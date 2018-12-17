from flask import Flask
from flask import request
import json
import os
import ankiport_core.quizlet_helper as qh
from flask import send_file
from flask import send_from_directory
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/yeet")
def yeet():
    return json.dumps({"good_word": "to HELL with georgia!"})


@app.route("/test")
def test():
    # return qh.apiTest("hello ")
    # return send_file("Calculus.apkg", attachment_filename="Calculus.apkg", as_attachment=True, mimetype="application/octet-stream")
    response = send_from_directory(
        os.getcwd(), "Calculus.apkg", as_attachment=True)
    response.headers["x-filename"] = "Calculus.apkg"

    response.headers["Access-Control-Expose-Headers"] = 'x-filename'
    return response
# return send_file("sylvester.png", attachment_filename="s.png", as_attachment=True)


@app.route('/query-example', methods=['POST'])
def query_example():
    # if key doesn't exist, returns None
    language = request.args.get('language')

    return '''<h1>The language value is: {}</h1>'''.format(language)


@app.route("/port")
def portQ():
    setID = request.args.get("setID")

    portResults = qh.portSet(setID)
    if (portResults[0]):
        response = send_from_directory(
            os.getcwd(), portResults[1] + ".apkg", as_attachment=True)
        response.headers["x-filename"] = portResults[1] + ".apkg"

        response.headers["Access-Control-Expose-Headers"] = 'x-filename'

        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers["Access-Control-Allow-Headers"] = "Origin, X-Requested-With, contentType,Content-Type, Accept, Authorization"
        response.headers["Access-Control-Allow-Methods"] = "GET,HEAD,OPTIONS,POST,PUT"
    # "<h3>Successfully ported set {}</h3>".format(portResults[1])
        return response
    else:
        return "<h3>Port failed :(</h3>"


if __name__ == '__main__':
    app.run(debug=True)
