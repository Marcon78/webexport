#!/usr/bin/env python
# -*- coding:utf-8 -*-
from app import db

class User(db.Model):
    __tablename__ = "tbl_user"

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    