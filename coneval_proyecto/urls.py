from django.urls import path
from coneval_proyecto import views

urlpatterns = [
    path('', views.index, name="index"),
    path('carencias', views.carencias, name="carencias"),
    path('index', views.index, name="index"),
    path('m_clasificacion', views.m_clasificacion, name="clasificacion"),
    path('prop_pobreza', views.pobreza, name="pobreza"),
]

