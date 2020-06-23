from django.db import models
from django.utils import timezone


# Create your models here.
class goals(models.Model):
    """docstring for goals"""
    goal=models.CharField(max_length=100)

    date_posted=models.DateTimeField()
    #author=models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.goal



