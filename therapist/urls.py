from django.urls import path
from .views import index, app, ai

urlpatterns = [
    path('', index, name='index'),
    path('app/', app, name='app'),
    path('ai/', ai, name='ai')
]
