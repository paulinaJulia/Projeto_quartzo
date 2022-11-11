from django.urls import path

from .views.contrato import ContratoUpdateView, ContratoCreateView, ContratoDeleteView, ContratoDetailView, ContratoListView


urlpatterns = [
    path('contrato-create/', ContratoCreateView.as_view(), name='contrato_create'),
    path('contrato-list/', ContratoListView.as_view(), name='contrato_list'),
    path('contrato-delete/<int:pk>/', ContratoDeleteView.as_view(), name='contrato_delete'),
    path('contrato-detail/<int:pk>/', ContratoDetailView.as_view(), name='contrato_detail'),
    path('contrato-update/<int:pk>/', ContratoUpdateView.as_view(), name='contrato_update'),
    
]
