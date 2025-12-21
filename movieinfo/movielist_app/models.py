from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    activate = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
