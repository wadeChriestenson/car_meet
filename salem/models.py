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
    host_name = models.CharField(max_length=100)
    meet_place = models.CharField(max_length=100)
    meet_address = models.CharField(max_length=100)
    meet_description = models.CharField(max_length=500)
    meet_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    enthusiast_type = models.CharField(max_length=1, choices=enthusiastChoices)
