from django.db import models


class NoiseLog(models.Model):
    timestamp = models.DateTimeField()
    decibel = models.DecimalField(max_digits=5, decimal_places=2)
