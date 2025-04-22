from django.urls import path
from .views import instagram_profile

urlpatterns = [
    path('profile/', instagram_profile),
]
