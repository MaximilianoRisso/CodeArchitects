from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

DEPARTMENT_CHOICES = [
    ("montevideo", "Montevideo"),
    ("canelones", "Canelones"),
]


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(error_messages={'required': ''})
    department = forms.CharField(label='Department', widget=forms.Select(choices=DEPARTMENT_CHOICES))
    phone = forms.IntegerField(required=False)
    name = forms.CharField(required=False)
    lastName = forms.CharField()

    class Meta:
        model = User
        fields = ['name', 'lastName', 'username', 'phone', 'email', 'department', 'password1', 'password2']

    def clean(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email exists")
        return self.cleaned_data

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None