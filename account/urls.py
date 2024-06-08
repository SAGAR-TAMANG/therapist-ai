from django.urls import path
from .views import login_view, register_user, logout_view, google_auth_receiver

urlpatterns = [
  path('login/', login_view, name="login"),
  path('register/', register_user, name="register"),
  path('logout/', logout_view, name="logout"),

  path('auth-receiver', google_auth_receiver, name='auth_receiver'),
]
