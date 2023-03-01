from django.db import models

# Create your models here.


class Count(models.Model):
  
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
