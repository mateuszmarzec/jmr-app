from django.db.models import Model, fields
from django.utils.crypto import get_random_string


class LongUrl(Model):
    url = fields.URLField()
    shortcut = fields.CharField(max_length=50, unique=True, default=get_random_string)
