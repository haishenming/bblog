from django.conf.urls import url
from . import views

app_name = 'app_users'
urlpatterns = [
    url(r'^register/', views.register, name='register'),
]