from django.urls import path, include
from .views import home, criar_compromisso, listar_compromissos
from django.contrib import admin


urlpatterns = [
    path('', home, name='A_TEA'),
    path('criar/', criar_compromisso, name='criar_compromisso'),
    path('listar/', listar_compromissos, name='listar_compromissos'),
]
