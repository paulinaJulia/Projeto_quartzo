from django.urls import path

from .views.contrato import ContratoUpdateView, ContratoCreateView, ContratoDeleteView, ContratoDetailView, ContratoListView
from .views.pagamento import PagamentoCreateView, PagamentoDetailView, PagamentoListView, update_item_pagamento

urlpatterns = [
    path('contrato-create/', ContratoCreateView.as_view(), name='contrato_create'),
    path('contrato-list/', ContratoListView.as_view(), name='contrato_list'),
    path('contrato-delete/<int:pk>/',
         ContratoDeleteView.as_view(), name='contrato_delete'),
    path('contrato-detail/<int:pk>/',
         ContratoDetailView.as_view(), name='contrato_detail'),
    path('contrato-update/<int:pk>/',
         ContratoUpdateView.as_view(), name='contrato_update'),
    path('pagamento-create/', PagamentoCreateView.as_view(),
         name='pagamento_create'),
    path('pagamento-list/', PagamentoListView.as_view(), name='pagamento_list'),
    path('pagamento-detail/<int:pk>',
         PagamentoDetailView.as_view(), name='pagamento_detail'),
    path('pagamento-item/<int:pagamento_pk>/<int:item_pagamento_pk>',
         update_item_pagamento, name='pagamento_item'),
]
