"""
Python Flask web application
"""
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def default():
    """
    Returns the default static webpage to the user.
    """
    return render_template("index.html")


@app.route("/greeter", methods=["GET"])
def greeter():
    """
    When calling this API endpoint you must supply a
    parameter called "name".

    Depending on the value of name, return different
    responses back to the user.
    """
    # Get the name of the user
    name = request.args.get("name")

    # Depending on the name, return a different response
    if name is None:
        response = "Hi anonymous, what is your name?"
    elif name == "Gordon Freeman":
        response = "Wake up Mr Freeman!"
    elif name == "Adam Jensen":
        response = "I never asked for this..."
    elif name in ["Obi Wan", "Obi-Wan", "Obi-Wan Kenobi"]:
        response = "Hello There!"
    elif name == "Heavy":
        response = "It costs four hundred thousand dollars to fire this weapon, for twelve seconds."
    else:
        response = f"Hi {name.title()}!"

    return response
