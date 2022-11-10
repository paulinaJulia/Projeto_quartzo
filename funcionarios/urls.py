from django.urls import path, include
from .views.funcionario_create_view import FuncionarioCreateView
from .views.funcionario_delete_view import FuncionarioDeleteView
from .views.funcionario_detail_view import FuncionarioDetailView
from .views.funcionario_list_view import FuncionarioListView
from .views.funcionario_update import FuncionarioUpdateView

urlpatterns = [
    path('funcionario-create/', FuncionarioCreateView.as_view(), name='funcionario_create'),
    path('funcionario-list/', FuncionarioListView.as_view(), name='funcionario_list'),
    path('funcionario-delete/<int:pk>/', FuncionarioDeleteView.as_view(), name='funcionario_delete'),
    path('funcionario-detail/<int:pk>/', FuncionarioDetailView.as_view(), name='funcionario_detail'),
    path('funcionario-update/<int:pk>/', FuncionarioUpdateView.as_view(), name='funcionario_update'),

]
