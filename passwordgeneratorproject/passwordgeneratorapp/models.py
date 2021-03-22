from django.db import models

# Create your models here.

"""model for Password"""
class Password(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=300)
    password = models.CharField(max_length=300)


    def __str__(self):
        return self.name

