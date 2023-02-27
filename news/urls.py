from django.urls import path
from .views import home, ArticoloDetailViewCB,ArticoloListView,GiornalistaDetailViewCB,GiornalistaListView 
from news.views import giornalisti_list_api, giornalista_api, tabella_giornalisti

app_name="news"

urlpatterns = [
    path('', home, name="homeview"),
    path('articoli/<int:pk>',ArticoloDetailViewCB.as_view(),name="articolo_detail"),
    path('lista_articoli/',ArticoloListView.as_view(),name="lista_articoli"),
    path('giornalisti/<int:pk>',GiornalistaDetailViewCB.as_view(),name="giornalista_detail"),
    path('lista_giornalisti/',GiornalistaListView.as_view(),name="lista_giornalisti"),
    path('giornalisti_lista_api/', giornalisti_list_api, name="lista_giornalisti_api"),
    path('giornalisti_lista_api/<int:pk>/', giornalista_api, name="giornalisti_api"),
    path('tabella_giornalisti/', tabella_giornalisti, name="tabella_giornalisti"),
]
