from django.shortcuts import render, redirect
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
#custom login view but now not need that, due to i used predefined views

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            print('using twitter')

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('dashboard')
                else:
                    messages.error(request, 'Invalid user')
                    return render(request, "account/login.html", {"form": form})  
            else:
                messages.error(request, 'Invalid credentials')
                return render(request, "account/login.html", {"form": form})  
    else:
        if request.user.is_authenticated:
            return redirect('dashboard')
        form = LoginForm()
        return render(request, "account/login.html", {"form": form})  


def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            #create new user object but avoid saving it yet
            new_user = user_form.save(commit=False)

            #cd = user_form.cleaned_data
            #set the chosen password
            new_user.set_password(user_form.cleaned_data['password']) # new_user.set_password(user_form.cleaned_data['password'])
            #save the user
            new_user.save()
            #create the user profile
            Profile.objects.create(user=new_user)
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
        return render(request, "account/register.html", {"user_form": user_form})

@login_required
def dashboard(request):
    context={'section': 'dashboard'}
    return render(request, "account/dashboard.html", context)                              

@login_required
def edit(request):    
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)

        profile_form = ProfileEditForm(instance=request.user.profile,data=request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')

        else:
            messages.error(request,'Error updating your profile')

    else:
        try:
            profile = User.objects.get(pk=request.user.id).profile
            #print('profile is present')
            #user_form=UserEditForm(instance=request.user)
            #profile_form = ProfileEditForm(instance=request.user.profile)
        except: 
            print('no profile')
            Profile.objects.create(user=request.user)
        user_form=UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)           
    return render(request, 'account/edit.html', {'user_form': user_form, 'profile_form': profile_form})        