from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Flask Imports
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, upgrade, migrate
from flask import Flask

# Importing configs
from config import config_dict

# For the database
db = SQLAlchemy()

def create_app(config_key='local'):
    app = Flask(__name__)
    # Enabling config initiation
    app.config.from_object(config_dict[config_key])
    config_dict[config_key].init_app(app)
    db = SQLAlchemy(app)
    db.init_app(app)
    migrate = Migrate(app, db)
    migrate.init_app(app, db)
    # register api
    from api import api as api_blueprint
    app.register_blueprint(api_blueprint)
    return app, db, migrate

app, db, migrate = create_app()

@app.cli.command()
def migrate():
    migrate()

@app.cli.command()
def upgrade():
    upgrade()


if __name__ == '__main__':
    config = config_dict['local']
    app.run(host=config.HOST,
            debug=True,
            port=config.PORT)
