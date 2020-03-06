from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserProfileForm
from delCampo.models import Profile


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            #default save
            user = form.save()
            #adding profile form content to user
            request.user.profile = user.profile
            request.user.profile.department = profile_form.cleaned_data['department']
            request.user.profile.phone = profile_form.cleaned_data['phone']
            request.user.profile.save()
            messages.success(request, f'Successfully Created Account!')
            return redirect("/login")
    else:
        form = UserRegisterForm()
        profile_form = UserProfileForm()
    return render(request, 'register.html', {'form': form, 'profile_form': profile_form})


def profile(request):
    return render(request, 'profile.html')