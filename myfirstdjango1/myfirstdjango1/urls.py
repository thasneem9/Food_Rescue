from django import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from core.views import index, contact, scoreboard
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', index, name='index'),
    path('items/', include('item.urls')),
    path('dashboard/',include('dashboard.urls')),
    path('contact/', contact, name='contact'),
    path('scoreboard/', scoreboard, name='scoreboard'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns +=staticfiles_urlpatterns()