from django.urls import path, include
from . import views

app_name = 'screenshot'

urlpatterns = [
    path('', views.index, name="index"),
    path('screenshot', views.screenshot, name="screenshot"),
]
