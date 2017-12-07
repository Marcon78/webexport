#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os

basedir = os.path.abspath(os.path.dirname(__file__))
# base_dir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv("WEBEXPORT_SECRET_KEY") or "this's@demo"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


# Development Environment
class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("WEBEXPORT_DEV_DB_URI") or \
        "sqlite:///" + os.path.join(basedir, "data-dev.sqlite")


# Test Environment
class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv("WEBEXPORT_DEV_DB_URI") or \
        "sqlite:///" + os.path.join(basedir, "data-test.sqlite")


# Simulation Environment
class SimConfig(Config):
    pass


# Real Environment
class RealConfig(Config):
    pass


# Online Environment
class OnlineConfig(Config):
    pass


CONST_CONFIG = {
    "development": DevConfig,
    "test": TestConfig,
    "simulation": SimConfig,
    "real": RealConfig,
    "online": OnlineConfig,
    "default": DevConfig
}