from peewee import SqliteDatabase, Model, TextField, IntegerField, CharField
import config

db = SqliteDatabase(config.BASE_NAME)


class Dream(Model):
    id = IntegerField()
    letter = CharField(max_length=1)
    title = TextField(primary_key=True)
    group = TextField()
    context = TextField()

    class Meta:
        database = db
