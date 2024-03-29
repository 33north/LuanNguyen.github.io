import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/index/")
def index():
    """
    """
    return render_template("index.html")



@app.route("/")
def home():
    """
    """
    return render_template("home.html")

@app.route("/about/")
def about():
    """
    """
    return render_template("about.html")

@app.route("/resume/")
def resume():
    """
    """
    return render_template("resume.html")

if __name__ == '__main__':
    app.run(host = "127.0.0.1", port = 5000, debug = True)