from django.db import models


class Data(models.Model):
    class Meta:
        ordering = ("year",)

    year = models.IntegerField()
    sale = models.IntegerField()
    country = models.CharField(max_length=15, null=True)
    product = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.product
