from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #custom login view
    #path('login/', views.user_login, name = 'login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(), name='login'),

    path('', views.dashboard, name='dashboard'),
    
    path('password_change/', auth_views.PasswordChangeView.as_view(), name="password_change"),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(),name="password_change_done"),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

    #alternate way to add all authentication views(including loginand logout, password change and reset, just add following line)
    #path('', include('django.contrib.auth.urls')),
]