from django.urls import path
from django.contrib.auth import views as auth_Views
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', auth_Views.LoginView.as_view(template_name ='accounts/login.html'), name='login'),
    path('logout/', auth_Views.LogoutView.as_view(), name ='logout'),
]