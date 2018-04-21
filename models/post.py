from mongoengine import Document, StringField, IntField, BooleanField, URLField

# create collection
# Service la ten class
class Post(Document):
    title = StringField()
    link = StringField()
    content = StringField()
