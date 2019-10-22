from django.shortcuts import render
from .forms import LoginForm
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

@login_required
def dashboard(request):
    context={'section': 'dashboard'}
    return render(request, "account/dashboard.html", context)                              