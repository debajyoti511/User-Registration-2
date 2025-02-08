from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('register', register, name='register'),
    path('user_login', user_login, name='user_login'),
    path('user_logout', user_logout, name='user_logout'),
    path('display_profile', display_profile, name='display_profile'),
    path('un', un, name='un'),
    path('otp', otp, name='otp'),
    path('change_pw', change_pw, name='change_pw'),
    path('change_new_password', change_pw, name='change_new_password'),
    path('login_with_otp', login_with_otp, name='login_with_otp'),
    path('loginotp', loginotp, name='loginotp')
]