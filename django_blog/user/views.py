from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() # Save
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form':form})


@login_required
def profile(request):
    if request.method == 'POST':
        # Update model and let mode form knpw what to expect in data
        form_user = UserUpdateForm(request.POST, instance=request.user)
        form_profile = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile) # Upload files as well
        if form_user.is_valid() and form_profile.is_valid():
            form_user.save()
            form_profile.save()
            messages.success(request, f'Account updated')
            return redirect('profile')
    else:
        form_user = UserUpdateForm(instance=request.user) # Pre popluate model forms
        form_profile = ProfileUpdateForm(instance=request.user.profile) # Pre popluate model forms
    context = {
        'form_user':form_user,
        'form_profile':form_profile
    }
    return render(request, 'user/profile.html', context=context)