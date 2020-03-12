from PIL import Image
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from delCampo.models import Profile

DEPARTMENT_CHOICES = [
    ("montevideo", "Montevideo"),
    ("canelones", "Canelones"),
]


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(error_messages={
        "unique": "Email is already associated to an account1"
    })
    first_name = forms.CharField(required=False, )
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',  'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.clean_password2())
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user


class UserProfileForm(ModelForm):
    class Meta:
        model = Profile
        department = forms.CharField(label='Department')
        phone = forms.IntegerField()
        fields = ('department', 'phone')


class UserUpdateForm(forms.ModelForm):

    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']

    def save(self, commit=True):

        user = super().save(commit=False)
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['imagePic', 'department', 'phone']
