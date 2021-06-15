from flask import Flask

signal_interpreter_app = Flask(__name__)


@signal_interpreter_app.route("/", methods=["GET"])
def hello():
    return "Hello World!!"


@signal_interpreter_app.route("/testPost", methods=["POST"])
def test_post():
    return "Hello World from Test Post call!!"
