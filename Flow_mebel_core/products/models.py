from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    cost = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return f'Product: {self.title}'


class Material(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'Material: {self.name}'


class Order(models.Model):
    SIZES = [
        ('s', 'small'),
        ('m', 'medium'),
        ('l', 'large')
    ]
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    size = models.CharField(max_length=20, choices=SIZES, default='m')
    material = models.ForeignKey(Material, on_delete=models.SET_DEFAULT, default=1)


class Image_for_prod(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
