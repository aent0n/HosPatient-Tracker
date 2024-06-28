from flask import Flask
from .fonctionsDB import db
import os

def create_app():
    app = Flask(__name__)


    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config.from_mapping(
        SQLALCHEMY_DATABASE_URI='mysql://root@127.0.0.1:3307/urgencesDB',
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

    # Initialisation de SQLAlchemy
    db.init_app(app)

    with app.app_context():
        from . import routes
        return app