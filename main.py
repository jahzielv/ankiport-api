from flask import Flask
from flask import request
from flask import send_file
from flask import send_from_directory
from flask import make_response
from flask_cors import CORS, cross_origin
import json
import os
import ankiport_core.quizlet_helper as qh

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello():
    return "<h2>Welcome to the Ankiport api!</h2>"


@app.route("/test")
def test():
    return json.dumps({"this_page": "API test"})


@app.route("/port")
def portQ():
    setID = request.args.get("setID")

    portResults = qh.portSet(setID)
    if (portResults[0]):
        # response = send_from_directory(
        #     os.getcwd(), portResults[1] + ".apkg", as_attachment=True)
        response = make_response(portResults[2].getvalue())

        response.headers["x-filename"] = portResults[1] + ".apkg"
        response.headers["Access-Control-Expose-Headers"] = 'x-filename'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers["Access-Control-Allow-Headers"] = "Origin, X-Requested-With, contentType,Content-Type, Accept, Authorization"
        response.headers["Access-Control-Allow-Methods"] = "GET,HEAD,OPTIONS,POST,PUT"

        return response
    else:
        return json.dumps({"status_code": portResults[1], "message": "Port failed. Check your set ID number!"}, indent=4)


if __name__ == '__main__':
    app.run(debug=True)
