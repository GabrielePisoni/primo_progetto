from django.urls import path
from .views import index_3, maxmin, media
app_name = "prova_pratica_0"
urlpatterns = [
    path('index_3', index_3, name='index_3'),
    path('maxmin', maxmin, name='maxmin'),
    path('media', media, name='media'),
]