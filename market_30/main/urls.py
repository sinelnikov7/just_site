from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import main_page

app_name = 'main'
urlpatterns = [
    path('', main_page, name='main_page'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)