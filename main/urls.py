from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('therapist.urls')),
    path('', include('account.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler500 = 'therapist.views.handler500'
handler404 = 'therapist.views.handler404'