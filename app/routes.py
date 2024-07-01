from flask import render_template
from .fonctionsDB import db
from app import create_app

app = create_app()

@app.route('/home/')
def home():
    return render_template('inscription.html')