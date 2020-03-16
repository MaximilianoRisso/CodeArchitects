from PIL import Image
from django.contrib.auth.models import User
from django.db import models

DEPARTMENT_CHOICES = [
    ("Montevideo", "Montevideo"),
    ("Canelones", "Canelones"),
]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagePic = models.ImageField(default='default.jpg', upload_to='profile_pics')
    phone = models.PositiveIntegerField(null=True)
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES, default='Montevideo')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, **kwargs):
        super().save()

        img = Image.open(self.imagePic.path)
        img.save(self.imagePic.path)

class Product(models.Model):

    imageProduct = models.ImageField(default='default.jpg', upload_to='product_pics')
    price = models.PositiveIntegerField(null=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class PendingOrder(models.Model):

    
    price = models.PositiveIntegerField(null=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'