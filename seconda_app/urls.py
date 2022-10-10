from django.urls import path
from .views import es_if, es_if_elif
app_name = "seconda_app"
urlpatterns = [
    path('es_if', es_if, name='es_if'),
    path('es_if_elif', es_if_elif, name='es_if_elif'),
]