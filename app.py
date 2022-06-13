from flask import Flask, escape, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return "index"


@app.route("/hello")
def hello_world():
    return "Hello, World!"


@app.route("/hello/<path:name>")  # path like string but can include /
def greet(name):
    # escape user inputs to prevent code injection
    return f"Hello, {escape(name)}!"


@app.route("/json")
def json_res():
    value1 = "value1"
    # jsonify() is called automatically on dict responses
    return {
        "key1": value1,
        "key2": "value2",
        "key3": "value3",
    }


@app.route("/tuple")
def tuple_res():
    # jsonify to return non-dict data types as json
    return jsonify(("first", "second"))
