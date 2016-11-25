from django.db import models

class book(models.Model):
    title = models.CharField(max_length=128, unique=True)
    authors = models.CharField(max_length=128, unique=True)
    publish = models.CharField(max_length=128, unique=True)
    pubDate = models.DateField(auto_now_add=True)
    version = models.IntegerField(default=1)
    price = models.IntegerField()
    
    
    def __str__(self):
        return self.title
    
    
    

