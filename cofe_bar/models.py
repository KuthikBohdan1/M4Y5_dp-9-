from django.db import models

class Review(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    author = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    
