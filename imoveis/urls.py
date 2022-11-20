from django.urls import path, include
from .views import ImovelDetailView, ImovelCreateView, ImovelDeleteView, ImovelListView, ImovelUpdateView

from .views import imovel_busca
urlpatterns = [
    #path('', home),
    path('imovel-create/', ImovelCreateView.as_view(), name='imovel_create'),
    path('imovel-list/', ImovelListView.as_view(), name='imovel_list'),
    path('imovel-delete/<int:pk>/', ImovelDeleteView.as_view(), name='imovel_delete'),
    path('imovel-detail/<int:pk>/', ImovelDetailView.as_view(), name='imovel_detail'),
    path('imovel-update/<int:pk>/', ImovelUpdateView.as_view(), name='imovel_update'),
    path('imovel-busca/', imovel_busca, name='imovel_busca'),
]
