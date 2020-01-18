import os

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from models import *
from app import app, db

SQLALCHEMY_DATABASE_NAME = 'test_db'
SQLALCHEMY_DATABASE_URI = f"postgresql://localhost/{SQLALCHEMY_DATABASE_NAME}"
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()