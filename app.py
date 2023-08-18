import os

from flask import Flask, flash, redirect, render_template, request, session
from tempfile import mkdtemp
from re import search

# Configure application
app = Flask(__name__)

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def kezdolap():
    """Betölti a kezdőlapot"""
    if request.method == "GET":
        return render_template("kezdolap.html")