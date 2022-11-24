from django.db import models

# Create your models here.

class Record(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre")

    def __str__(self):
        return "%s" %(self.name)