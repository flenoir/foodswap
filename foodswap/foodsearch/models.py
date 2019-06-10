from django.db import models

# Create your models here.

class Product(models.Model):

    def __str__(self):
        return self.product_name

    # We specify the model fields
    product_name = models.CharField(max_length=100)
    brands = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=200, null=True)
    product_url = models.CharField(max_length=150, null=True)
    product_code = models.CharField(max_length=20, null=True)
    product_image = models.CharField(max_length=100, null=True)
    nutriscore = models.CharField(max_length=1, null=True)
    stores = models.CharField(max_length=150, null=True)
    quantity = models.CharField(max_length=40, null=True)
    