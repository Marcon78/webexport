#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
from flask_script import Manager, Server
from flask_script.commands import Clean
from flask_migrate import Migrate, MigrateCommand

from app import db, create_app
from app.models import User

app = create_app(os.getenv("WEBEXPORT_CONFIG") or "default")

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command("server", Server(host='0.0.0.0', port=5000))
manager.add_command("clean", Clean)
manager.add_command("db", MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app=app, db=db,
                User=User)


@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == "__main__":
    manager.run()