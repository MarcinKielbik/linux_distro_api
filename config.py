import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(BASE_DIR, "database.db")}'  # SQLite
    # SQLALCHEMY_DATABASE_URI = "postgresql://user:password@localhost/mydatabase"  # PostgreSQL
    # SQLALCHEMY_DATABASE_URI = "mysql://user:password@localhost/mydatabase"  # MySQL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
