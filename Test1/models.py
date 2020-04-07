from django.db import models
from django.utils import timezone

class testModel(models.Model):
    nombre = models.CharField(max_length=255, null=True)
    apellido_paterno = models.CharField(max_length=255, null=True)
    apellido_materno = models.CharField(max_length=255, null=True)
    edad = models.IntegerField(null=True)
    active = models.BooleanField(default = False)
    def __str__(self):
        return self.testName

    class Meta:
        db_table = "testModel"
# Create your models here.
