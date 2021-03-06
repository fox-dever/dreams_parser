from peewee import SqliteDatabase, Model, TextField, IntegerField, CharField
import config

db = SqliteDatabase(config.BASE_NAME)


class Dream(Model):
    id = CharField(max_length=4, primary_key=True)
    letter = CharField(max_length=1)
    title = CharField(max_length=25)
    group = CharField(max_length=25)
    context = TextField()

    class Meta:
        database = db
        
        
class DataBase:

    def __init__(self):
        db.connect()
        db.create_tables([Dream])

    def write(self, data):
        print('Writing data to base')

        with db.atomic():
            Dream.insert_many(data).execute()
