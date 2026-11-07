from django.db import models
from datetime import datetime, date

class Tasks(models.Model):
    title = models.CharField()
    caption = models.CharField()
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(default= datetime.now())
