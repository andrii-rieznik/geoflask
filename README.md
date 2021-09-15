# Geoflask

This project fully placed in Docker.

There are two ways to setup environment and run application via Docker:

1. [Visual Studio Code Remote](https://code.visualstudio.com/docs/remote/containers) - open project in VS Code.

1. Build manually from shell on any machine with docker.

## 📌 Requirements

- [Docker](https://www.docker.com/).


## 🔧 Setup

0. Install `remote-containers` Visual Studio Code extensions.

    ```bash
    > code --install-extension ms-vscode-remote.remote-containers
    ```

1. Clone this repo to your machine.

    ```bash
    > git clone git@github.com:andrejreznik/geoflask.git
    ```

2. Open Visual Studio Code in `geoflask` folder:

    ```bash
    > cd geoflask
    > code .
    ```

    or build manually **(skip if using VS Code)**.

    ```bash
    > cd geoflask
    > docker-compose build .
    ```

3. Prepare database:

    ```bash
    > export FLASK_APP=geoflask/web/commands.py
    > flask create-db
    > flask seed-db
    ```

## 🚀 Run application

1. To start `Flask` server you need to start process in terminal:

    ```bash
    > export FLASK_APP=geoflask/web/app.py
    > flask run
    ```

    or simply [launch](.vscode/launch.json) application by click on `Run` -> `Run Without Debugging` <kbd>Ctrl</kbd> + <kbd>F5</kbd>,

    or via `docker-compose` command:
    ```bash
    > docker-compose exec -e FLASK_APP=geoflask/web/app.py web python run
    ```


## 📚 Libraries

- [Flask](https://github.com/pallets/flask) - micro web framework.
- [GeoAlchemy2](https://github.com/geoalchemy/geoalchemy2) - geospatial extension to SQLAlchemy.
- [Flask-SQLAlchemy](https://github.com/pallets/flask-sqlalchemy) - extension for Flask that adds support  for SQLAlchemy.
- [Flask-Migrate](https://github.com/miguelgrinberg/Flask-Migrate) - database migrations.
- [psycopg2](https://github.com/psycopg/psycopg2) - PostgreSQL Database Adapter.
- [uWSGI](https://github.com/unbit/uwsgi) - web server.
- [flake8](https://github.com/PyCQA/flake8) - linter and formatter.


## ⚖️ Licensing

See: [LICENSE (MIT)](LICENSE).
