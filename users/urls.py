from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('', views.log_in),
    path('registrar', views.sign_up),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout', views.log_out),
    path('profile', views.profile),
]
