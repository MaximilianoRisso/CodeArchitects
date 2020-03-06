from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models

DEPARTMENT_CHOICES = [
    ("Montevideo", "Montevideo"),
    ("Canelones", "Canelones"),
]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    phone = models.PositiveIntegerField(null=True)
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES, default='Montevideo')

    def __str__(self):
        return f'{self.user.username} Profile'
