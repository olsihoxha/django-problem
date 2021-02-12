from django.db import models


class CountryName1(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class TeslaModel1(models.Model):
    model_name = models.CharField(max_length=30)
    price = models.IntegerField()
    origin = models.ForeignKey(CountryName1, on_delete=models.CASCADE, related_name='teslamodels')

    def __str__(self):
        return self.model_name
