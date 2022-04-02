from django.db import models

enthusiastChoices = (
    ("1", "JDM"),
    ("2", "USDM"),
    ("3", "EDM"),
)


# Create your models here.
class meetInfo(models.Model):
    latitude = models.CharField(max_length=10)
    longitude = models.CharField(max_length=10)
    hostName = models.CharField(max_length=100)
    meetPlace = models.CharField(max_length=100)
    meetAddress = models.CharField(max_length=100)
    meetDescription = models.CharField(max_length=500)
    meetDate = models.DateField()
    startTime = models.TimeField()
    endTime = models.TimeField()
    enthusiastType = models.CharField(max_length=1, choices=enthusiastChoices)
