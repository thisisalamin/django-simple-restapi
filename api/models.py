from django.db import models
from datetime import datetime


class Note(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    created_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return '%s %s' % (self.title, self.body)
