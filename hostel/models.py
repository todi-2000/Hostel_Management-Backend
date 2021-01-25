from django.db import models


Hostel_Category = [
    ('Government','Government'),
    ('Semi-Government','Semi-Government'),
    ('Private','Private')
]

Hostel_Type = [
    ('None','None'),
    ('Boys','Boys'),
    ('Girls','Girls')
]
# Create your models here.
class HostelDetail(models.Model):
    """
    Hostel Details
    """
    name = models.CharField(max_length=2000)
    description = models.TextField(max_length=100000)
    category = models.CharField(max_length=1000, choices=Hostel_Category)
    type = models.CharField(max_length=1000, choices=Hostel_Type, default="None")
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=500)
    city = models.CharField(max_length=200)
    fees = models.IntegerField()
    total_rooms = models.IntegerField()
    vacant_rooms = models.IntegerField()

    def __str__(self):
        return self.name

