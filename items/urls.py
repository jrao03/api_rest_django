from django.urls import path
from . import views

urlpatterns = [
    path('items', views.get_item),
    path('borrar/<int:id>/', views.delete_item),
    path('actualizar/<int:id>/', views.update_item),
    path('actualizar/<int:id>/parcial/', views.partial_update_item),
    path('insertar', views.insert_item),
]
