from django.contrib.auth.forms import UserCreationForm
from django.db import models

# Create your models here.


class UserRegisterForm(UserCreationForm):
    email = models.EmailField(unique=True, )
    phone = models.IntegerField(max_length=9,)
