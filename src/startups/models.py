from django.db import models

# Create your models here.

class Startup(models.Model):
    name = models.CharField(max_length=30)
    # founders = models.CharField(max_length=100, default="-")
    # investors = models.CharField(max_length=200, default="-")
    # # total_funding = models.DecimalField(max_digits=50, decimal_places=1, default=0)
    # # latest_funding = models.DecimalField(max_digits=50, decimal_places=1, default=0)
    # description = models.TextField(default="-")

    def __str__(self):
        return self.name
