from django.urls import path
from news.views import inicio_view, models_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', inicio_view, name='inicio_view'),
    path("Models/", models_view, name="models_view")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)