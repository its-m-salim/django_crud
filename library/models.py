from django.db import models



class Book(models.Model):
    title = models.CharField()
    genre = models.CharField()
    author = models.CharField()
    year = models.IntegerField()
    caption = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)