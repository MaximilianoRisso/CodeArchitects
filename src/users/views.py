from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserProfileForm, ProfileUpdateForm, UserUpdateForm
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


@login_required
def profile(request):
    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        profile_update_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_update_form.is_valid() and profile_update_form.is_valid():
            user = user_update_form.save()
            request.user.profile = user.profile
            request.user.profile.imagePic = profile_update_form.cleaned_data['imagePic']
            request.user.profile.department = profile_update_form.cleaned_data['department']
            request.user.profile.phone = profile_update_form.cleaned_data['phone']
            request.user.profile.save()

            profile_update_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('/profile')

    else:
        user_update_form = UserUpdateForm(instance=request.user)
        profile_update_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_update_form': user_update_form,
        'profile_update_form': profile_update_form
    }

    return render(request, 'profile.html', context)
