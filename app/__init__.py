#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy

from config import CONST_CONFIG
from . import views

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(CONST_CONFIG[config_name])

    CONST_CONFIG[config_name].init_app(app)

    db.init_app(app)

    from app.controllers.main import main as blueprint_main
    app.register_blueprint(blueprint_main)

    return app