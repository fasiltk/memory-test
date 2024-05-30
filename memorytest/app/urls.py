from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('display/', display, name='display'),
    path('item/',item,name='item'),
    path('hidden/',hidden,name='hidden'),
    path('check/<int:id>/', check, name='check'),
    path('win/',win,name='win'),
    path('lose/',lose,name='lose')    
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
