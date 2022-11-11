from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),
    path('cliente/', include('clientes.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('imovel/', include('imoveis.urls')),
    path('funcionario/', include('funcionarios.urls')),
    path('financeiro/', include('financeiro.urls')),
]
