from django.shortcuts import render
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
#custom login view but now not need that, due to i used predefined views
'''
def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Authenticated Successfuly")
                else:
                    return HttpResponse("Disabled Account")
            else:
                return HttpResponse("Invalid Login")
    else:
        form = LoginForm()
        return render(request, "account/login.html", {"form": form})  
'''

def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            #create new user object but avoid saving it yet
            new_user = user_form.save(commit=False)

            cd = user_form.cleaned_data
            #set the chosen password
            new_user.set_password(cd['password']) # new_user.set_password(user_form.cleaned_data['password'])
            #save the user
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
        return render(request, "account/register.html", {"user_form": user_form})

@login_required
def dashboard(request):
    context={'section': 'dashboard'}
    return render(request, "account/dashboard.html", context)                              