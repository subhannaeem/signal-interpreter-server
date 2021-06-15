from flask import Flask, request, jsonify
from json_parser import JsonParser


signal_interpreter_app = Flask(__name__)
json_parser = JsonParser()


@signal_interpreter_app.route("/", methods=["GET"])
def hello():
    return "Hello World!!"


@signal_interpreter_app.route("/testPost", methods=["POST"])
def test_post():
    return "Hello World from Test Post call!!"


@signal_interpreter_app.route("/getSignal", methods=["POST"])
def interpret_signal():
    data = request.get_json()
    signal_title = json_parser.get_title(data["signal_id"])
    return jsonify(signal_title)
