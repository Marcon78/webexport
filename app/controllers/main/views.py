#!/usr/bin/env python
# -*- coding:utf-8 -*-
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import render_template, current_app
from app import db

from . import main

@main.route("/")
def index():
    engine = create_engine(current_app.config["SQLALCHEMY_DATABASE_URI"],
                        convert_unicode=True)
    metadata = MetaData()
    db_session = scoped_session(sessionmaker(autocommit=False,
                                            autoflush=False,
                                            bind=engine))

    s = db_session()
    res = s.execute("SELECT * FROM tbl_saleinfo;").fetchall()
    return render_template("index.html", res=res)