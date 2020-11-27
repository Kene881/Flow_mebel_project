from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    cost = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f'Product: {self.title}'

class Registration(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=8)
    email = models.CharField(max_length=255)

    def __str__(self):
        return f'Data: {self.title}'