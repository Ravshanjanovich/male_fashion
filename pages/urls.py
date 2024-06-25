from django.urls import path
from pages.views import HomePage, ContactView


app_name = 'pages'


urlpatterns = [
    path("", HomePage.as_view(),name='home'),
    path("contact/", ContactView.as_view(), name='contact')
]