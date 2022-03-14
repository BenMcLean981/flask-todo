"""
Database global singleton

There are also a few type annotations
that help me here. However, there is a
problem with flask_sqlalchemys typings
and this actually isn't perfect.
"""
from typing import Type

import flask_sqlalchemy
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

Model: Type[flask_sqlalchemy.Model] = db.Model
Column: Type[sqlalchemy.Column] = db.Column

Integer: Type[sqlalchemy.Integer] = db.Integer
String: Type[sqlalchemy.String] = db.String
Text: Type[sqlalchemy.Text] = db.Text
DateTime: Type[sqlalchemy.DateTime] = db.DateTime
Float: Type[sqlalchemy.Float] = db.Float
Boolean: Type[sqlalchemy.Boolean] = db.Boolean
PickleType: Type[sqlalchemy.PickleType] = db.PickleType
LargeBinary: Type[sqlalchemy.LargeBinary] = db.LargeBinary

ForeignKey: Type[sqlalchemy.ForeignKey] = db.ForeignKey
relationship: Type[sqlalchemy.orm.relationship] = db.relationship
