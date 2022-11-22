from django.urls import path, include
from .views.cliente.cliente_create_view import ClienteCreateView
from .views.cliente import ClienteUpdateView, ClienteDeleteView, ClienteDetailView, ClienteListView
from .views.funcionario import  FuncionarioCreateView, FuncionarioDeleteView, FuncionarioDetailView,FuncionarioListView, FuncionarioUpdateView

urlpatterns = [
    #path('', home),
    path('cliente-create/', ClienteCreateView.as_view(), name='cliente_create'),
    path('cliente-list/', ClienteListView.as_view(), name='cliente_list'),
    path('cliente-delete/<int:pk>/', ClienteDeleteView.as_view(), name='cliente_delete'),
    path('cliente-detail/<int:pk>/', ClienteDetailView.as_view(), name='cliente_detail'),
    path('cliente-update/<int:pk>/', ClienteUpdateView.as_view(), name='cliente_update'),

    path('funcionario-create/', FuncionarioCreateView.as_view(), name='funcionario_create'),
    path('funcionario-list/', FuncionarioListView.as_view(), name='funcionario_list'),
    path('funcionario-delete/<int:pk>/', FuncionarioDeleteView.as_view(), name='funcionario_delete'),
    path('funcionario-detail/<int:pk>/', FuncionarioDetailView.as_view(), name='funcionario_detail'),
    path('funcionario-update/<int:pk>/', FuncionarioUpdateView.as_view(), name='funcionario_update'),

]
