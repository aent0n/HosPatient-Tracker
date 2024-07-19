from flask import render_template, request, redirect, url_for
from flask import current_app as app
from . import db
from .fonctionsDB import *


@app.route('/')
def index():
    return render_template('acceuil_accompagnant.html')

@app.route('/inscription')
def inscription():
    return render_template('inscription.html')