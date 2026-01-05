#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route("/print/<parameter>")
def print_parameter(parameter):
    print("hello")
    return "hello"

@app.route("/count/<int:parameter>")  # ADD <int:> to convert to integer
def count_parameter(parameter):
    result = ""
    for param in range(parameter):
        result += f"{param}\n"  # Convert to string and add newline
    return result

@app.route("/math/<path:parameters>")
def math_param(parameters):
    a, op, b = parameters.split("/")
    a, b = int(a), int(b)

    ops = {
        "+": a + b,
        "-": a - b,
        "*": a * b,
        "div": a / b,
        "%": a % b
    }

    return str(ops[op])
if __name__ == '__main__':
    app.run(port=5555, debug=True)
