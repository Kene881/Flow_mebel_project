from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    cost = models.CharField(max_length=50)
    def __str__(self):
        return f'Product: {self.title}'

class Image_for_prod(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)