from django.urls import path
from .views import update_profile

urlpatterns = [
    path('perfil/editar/', update_profile, name='update_profile'),
]
