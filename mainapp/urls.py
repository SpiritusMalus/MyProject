from django.template.defaulttags import url

from myproject import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Main.as_view(), name='main'),
    path('register/', Registration.as_view(), name='register'),
    path('basket/', include(('basketapp.urls', 'basketapp'), namespace='basket')),
    path('', include('social_django.urls', namespace='social')),
    path('', include('django.contrib.auth.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
