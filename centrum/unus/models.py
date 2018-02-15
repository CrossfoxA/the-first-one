from django.db import models
# Create your models here.

class unusListElements(models.Model):
    list_element = models.CharField(max_length=255)
    done = models.BooleanField()
    