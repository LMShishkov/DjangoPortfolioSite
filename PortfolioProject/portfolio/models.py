from django.db import models
from datetime import date

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)
    start_date = models.DateField(blank=True, default=date.today)
    end_date = models.DateField(blank=True, default=date.today)
