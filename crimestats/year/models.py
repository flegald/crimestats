"""Year models."""
from django.db import models


class Years(models.Model):
    """Year object."""

    year = models.CharField(max_length=255, null=True, blank=True)
    population = models.CharField(max_length=255, null=True, blank=True)
    total = models.CharField(max_length=255, null=True, blank=True)
    violent = models.CharField(max_length=255, null=True, blank=True)
    prop = models.CharField(max_length=255, null=True, blank=True)
    murder = models.CharField(max_length=255, null=True, blank=True)
    rape = models.CharField(max_length=255, null=True, blank=True)
    robbery = models.CharField(max_length=255, null=True, blank=True)
    assault = models.CharField(max_length=255, null=True, blank=True)
    burglary = models.CharField(max_length=255, null=True, blank=True)
    theft = models.CharField(max_length=255, null=True, blank=True)
    gta = models.CharField(max_length=255, null=True, blank=True)



