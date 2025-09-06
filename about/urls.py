from django.urls import path
from . import views

app_name = 'about'

urlpatterns = [
    # Add your URL patterns here
    path('', views.index, name='index'),
]
