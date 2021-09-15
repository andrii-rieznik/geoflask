import json

from .app import app
from .db import recreate_database, session_scope
from .models import Location


@app.cli.command("create-db")
def create_db():
    recreate_database()


@app.cli.command("seed-db")
def seed_db():
    with open("tests/sample_data/locations.json", "r") as f:
        locations = json.load(f)

    with session_scope() as s:
        for location in locations:
            # TODO: should be changed to something like find_or_create
            s.add(Location(**location))
