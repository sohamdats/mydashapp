from django.db import models
from mongoengine import *

# Create your models here.
class Container(EmbeddedDocument):
    _id = StringField(required=True)
    name = StringField(required=True)
    cpu_usage = StringField(required=True)
    memory_usage  = StringField(required=True)


class Timestamp(Document):
    time = StringField(required=True)
    stats = ListField(EmbeddedDocumentField(Container))


    
