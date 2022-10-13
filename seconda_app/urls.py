from django.urls import path
from .views import es_if, es_if_elif, es_for, index_2
app_name = "seconda_app"
urlpatterns = [
    path('es_if', es_if, name='es_if'),
    path('es_if_elif', es_if_elif, name='es_if_elif'),
    path('es_for', es_for, name='es_for'),
    path('index_2', index_2, name='index_2'),
]