from peewee import Model, CharField, TextField, SQL
from database.database import dblog

class Blog(Model):
    Titulo=CharField(max_length=200)
    Autor=CharField()
    Materia=TextField()

    class Meta:
        database=dblog