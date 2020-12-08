from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class Tutorial(models.Model):
    Tittle = models.CharField(max_length=200)
    Date_Published = models.DateTimeField()
    Contant = HTMLField()

    def __str__ (self):
        return self.Tittle
