from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import importlib
import os

from app import app, db
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

MODELS_DIRECTORY = "app/models"
EXCLUDE_FILES = ["__init__.py"]

def import_model():
    for dir_path, dir_names, file_names in os.walk(MODELS_DIRECTORY):
        for file_name in file_names:
            if file_name.endswith(".py") and not file_name in EXCLUDE_FILES:
                file_path = os.path.join(dir_path, file_name)
                module_name = file_path.replace(os.sep, ".").replace('.py', '')
                importlib.import_module(module_name)

if __name__ == '__main__':
    import_models()
    manager.run()
