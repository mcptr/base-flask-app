import flask
import json


app = flask.Flask(__name__)


def log_request(req_dict):
    """Stores request information in db"""
    with open("log-requests.txt", "a+") as fh:
        fh.write(json.dumps(req_dict))


if __name__ == "__main__":
    app.run(debug=True)
