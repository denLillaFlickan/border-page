import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp

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

@app.route("/kapcsolat")
def kapcsolat():
    """Betölti a kapcsolat oldalt"""
    if request.method == "GET":
        return render_template("kapcsolat.html")
    
@app.route("/bemutatkozas")
def bemutatkozas():
    """Betölti a bemutatkozás oldalt"""
    if request.method == "GET":
        return render_template("bemutatkozas.html")

@app.route("/szolgaltatasok")
def szolgaltatasok():
    """Betölti a szolgáltatások oldalt"""
    if request.method == "GET":
        return render_template("szolgaltatasok.html")
