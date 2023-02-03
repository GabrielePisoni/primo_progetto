from django.urls import path
from .views import contatti

urlpatterns = [
    path('contattaci/', contatti, name='contatti')
]