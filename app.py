import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    """
    """
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug = True)