from django.urls import path
from news.views import inicio_view, models_view

urlpatterns = [
    path('', inicio_view, name='inicio_view'),
    path("Models/", models_view, name="models_view")
]
