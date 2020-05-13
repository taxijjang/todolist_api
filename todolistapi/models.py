from django.db import models
from pytz import timezone

class DoList(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    published_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class DoneList(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    published_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title