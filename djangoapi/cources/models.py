from django.db import models

# Create your models here.
class Cource(models.Model):
    # ghg
    name = models.CharField(max_length = 200)
    language = models.CharField(max_length = 100)
    price =models.CharField(max_length = 10)