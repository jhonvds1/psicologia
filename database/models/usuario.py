from peewee import Model, CharField
from database.database import db

class Usuario(Model):
    Nome=CharField()
    Email=CharField()

    class Meta:
        database=db