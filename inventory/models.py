from django.db import models


class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True, verbose_name='Name')
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    description = models.CharField(max_length=255)
    quantity_sqft = models.FloatField(default=0.0)
    quantity_pcs = models.FloatField(default=0.0)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
