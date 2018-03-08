from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'app_users'
urlpatterns = [
    url(r'^register/', views.register, name='register'),
    path('<username>/home/', views.home, name='user_home')
]