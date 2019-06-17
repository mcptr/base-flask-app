import flask
import json


app = flask.Flask(__name__)


def log_request(req_dict):
    """Stores request information in db"""
    with open("tmp/requests.log", "a+") as fh:
        fh.write(json.dumps(req_dict) + "\n")


@app.after_request
def log_request_callbacks(response):
    log_request(dict(
        remote_addr=flask.request.remote_addr,
        path=flask.request.path,
    ))

    return response


if __name__ == "__main__":
    app.run(debug=True)
