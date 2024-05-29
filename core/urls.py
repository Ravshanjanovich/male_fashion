from django.contrib import admin
from django.urls import path, include
from django.conf.urls import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    
]


urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns +=  media(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
