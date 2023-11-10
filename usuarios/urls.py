from django.urls import path
from usuarios.views import login, cadastro

urlpatterns = [
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro'),
    # TODO - Create logout page: path('logout', logout, name='logout'),
]