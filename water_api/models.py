from django.db import models

class WaterQuality(models.Model):

    time = models.DateTimeField(auto_now=False, auto_now_add=False)
    temperature = models.FloatField(null=True)
    clarity = models.FloatField(null=True)
    conductivity = models.FloatField(null=True)
    pH = models.FloatField(null=True)
    alkalinity = models.FloatField(null=True)
    chlorine = models.FloatField(null=True)
    oxygen_dissolved = models.FloatField(null=True)
    hardness = models.FloatField(null=True)

    def __str__(self):
        return f"Water Reading - {self.time}"
    
    # f"{self.time} - {self.temperature} - {self.clarity} - {self.conductivity} - {self.pH} - {self.alkalinity} - {self.chlorine} - {self.oxygen_dissolved} - {self.hardness}"