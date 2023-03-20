from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    # path('list/', views.list), # URL para vista mediante metodo
    path('list/', views.listGeneric.as_view()) # URL para vista creada mediante vista generica.
    # En este caso es necesario poner al final de la llamada a la vista el método as_view
]
