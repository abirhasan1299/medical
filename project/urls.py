from django.contrib import admin
from django.urls import path,include
from .views import home,about
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('admin/', admin.site.urls),
    path('medicine/', include('medicine.urls')),
    path('doctor/', include('doctor.urls')),
    # path('inbox/notifications/', include('notifications.urls', namespace='notifications')),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
