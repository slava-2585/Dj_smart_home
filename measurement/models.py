from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor (models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=300)


class Measurement(models.Model):
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurement')