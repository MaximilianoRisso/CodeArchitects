
# Create your models here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models


class UserRegisterForm(UserCreationForm):
    email = models.EmailField(error_messages={
        "unique": "Email is already associated to an account1"
    })

    first_name = models.CharField()
    last_name = models.CharField()


