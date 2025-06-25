from django.db import models

class Review(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    author = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    
    def __str__(self):
        return f"Title: {self.title}\nContent: {self.content}\nAuthor: {self.author}\nPublished: {self.pub_date}"