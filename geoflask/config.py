import os


def get_url_from_envs():
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')
    database = os.getenv('DB_DATABASE')

    return f"postgresql://{user}:{password}@{host}:{port}/{database}"


class Config:
    SQLALCHEMY_DATABASE_URI = get_url_from_envs()
    SQLALCHEMY_TRACK_MODIFICATIONS = False
