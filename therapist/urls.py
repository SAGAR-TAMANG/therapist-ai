from django.urls import path, re_path
from .views import index, app, ai

urlpatterns = [
    path('', index, name='index'),
    path('app/', app, name='app'),
    path('ai/', ai, name='ai'),

    # Matches any html file
    # re_path(r'^.*\.*', pages, name='pages'),
]
