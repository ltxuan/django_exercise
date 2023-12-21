from django.db import models

# Create your models here.
class postForm(models.Model):
    title = models.CharField(max_length = 25)
    body = models.TextField()
    create_at = models.DateTimeField(auto_now_add = True)
    
    def __str__(selt):
        return selt.title