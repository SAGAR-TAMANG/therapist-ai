from django.urls import path
from .views import index, app

urlpatterns = [
    path('', index, name='index'),
    path('app/', app, name='app'),
]
