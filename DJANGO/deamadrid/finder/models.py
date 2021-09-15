from django.db import models

# Create your models here.
class DEA(models.Model):
    dea_code = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=10)
    availability = models.CharField(max_length=100)
    x = models.IntegerField()
    y = models.IntegerField()



    
