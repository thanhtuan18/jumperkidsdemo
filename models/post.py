from mongoengine import Document, StringField, IntField, BooleanField, URLField

class Post(Document):
    title = StringField()
    link = StringField()
    content = StringField()
