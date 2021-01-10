from django.db import models

# Create your models here.
class dataLine(models.Model):
    date=models.CharField(max_length=12)
    rentCount=models.FloatField()
    hour=models.FloatField()
    temperature=models.FloatField()
    humidity=models.FloatField()
    windSpeed=models.FloatField()
    visibility=models.FloatField()
    dewPointTemp=models.FloatField()
    solarRadiation=models.FloatField()
    rainfall=models.FloatField()
    snowfall=models.FloatField()
    seasons=models.CharField(max_length=8)
    holiday=models.BooleanField()
    functDay=models.BooleanField()
    
