import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import App, db
from models import Client

App.config.from_object("config.Config")
migrate = Migrate(App, db)
manager = Manager(App)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()