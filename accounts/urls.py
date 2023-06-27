from django.urls import path, include

from . import views

app_name = 'accounts'

urlpatterns = [
    # Inclui URLs de autenticação default
    path('', include('django.contrib.auth.urls')),
    # Página de cadastro
    path('register/', views.register, name='register'),
]
