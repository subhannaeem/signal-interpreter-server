from flask import Flask, request

signal_interpreter_app = Flask(__name__)


@signal_interpreter_app.route("/", methods=["GET"])
def hello():
    return "Hello World!!"


@signal_interpreter_app.route("/", methods=["POST"])
def test_post():
    data = request.get_json()
    return data
