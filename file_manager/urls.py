from django.urls import path
from . import views

urlpatterns = [
    path('upload', views.subir_archivo),
]
