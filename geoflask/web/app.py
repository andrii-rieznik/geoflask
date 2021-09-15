from flask import Flask
from flask import jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from .db import session_scope
from .models import Location
from ..config import Config


db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    return app


app = create_app()


@app.route("/")
def index():
    with session_scope() as s:
        locations = s.query(Location).all()

    return jsonify([Location.to_dict(location) for location in locations])


if __name__ == '__main__':
    app.run(debug=True)
