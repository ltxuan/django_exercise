from django.db import models

# Create your models here.
class contactFrom(models.Model):
    usename = models.CharField(max_length = 25)
    email = models.EmailField()
    body = models.TextField()
    
    def __str__(selt):
        return selt.usename