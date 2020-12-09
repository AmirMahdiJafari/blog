from django.db import models
from tinymce.models import HTMLField
from datetime import datetime
# Create your models here.
class TutorialCategory(models.Model):
    category = models.CharField(max_length = 200)
    summery = models.CharField(max_length = 200)
    slug = models.CharField(max_length = 200)

    def __str__(self):
        return self.category

class TutorialSeries(models.Model):
    Series = models.CharField(max_length = 200)
    Summery = models.CharField(max_length = 200)
    Category = models.ForeignKey(TutorialCategory , on_delete=models.SET_DEFAULT , verbose_name='Category', default = 'some string')
    class meta:
        verbose_name_plural = 'Series'

    def __str__(self):
        return self.Series


class Tutorial(models.Model):
    Tittle = models.CharField(max_length=200)
    Date_Published = models.DateTimeField(datetime.now())
    Contant = HTMLField()
    Tutorial_Series = models.ForeignKey(TutorialSeries , on_delete=models.SET_DEFAULT, verbose_name = "Series", default = 1 )
    Tutorial_slug = models.CharField(max_length = 200)

    def __str__ (self):
        return self.Tittle
