from django.urls import path
from users.views import ProfileView, logout_view, user_registration, login_view

app_name = 'user'

urlpatterns = [
    path("profile/", ProfileView.as_view(), name='profile'),
    path("logout/", logout_view, name='logout'),
    path("login/", login_view, name='login'),
    path("registration/", user_registration, name='registration')
]