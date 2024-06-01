from django.urls import path
from .consumers import ChatConsumerDemo

websocket_urlpatterns = [
  path("ws/ai-demo/", ChatConsumerDemo.as_asgi()),
]