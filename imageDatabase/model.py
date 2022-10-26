from enum import Enum

import mongoengine as me


class Type(Enum):
    FILE = 'File'
    URL = 'URL'


class Image(me.Document):
    meta = {'collection': 'images'}

    title = me.StringField(required=True, unique=True)
    type = me.EnumField(Type, required=True, default=Type.FILE)
    url = me.URLField(required=False)
    path = me.StringField(required=False)
    descriptors = me.ListField(required=True)
    # keypoints = me.ListField(required=True)
