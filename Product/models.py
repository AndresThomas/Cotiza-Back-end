from django.db import models

# Create your models here.
class Product(models.Model):
    id =  models.AutoField(primary_key=True)
    folio =  models.CharField(max_length=30)
    descripcion = models.CharField(max_length=255)
    costo = models.FloatField()
    cantidad = models.IntegerField()