from django.urls import path, include
from .views.cliente_create_view import ClienteCreateView
from .views import ClienteUpdateView, ClienteDeleteView, ClienteDetailView, ClienteListView

urlpatterns = [
    #path('', home),
    path('cliente-create/', ClienteCreateView.as_view(), name='cliente_create'),
    path('cliente-list/', ClienteListView.as_view(), name='cliente_list'),
    path('cliente-delete/<int:pk>/', ClienteDeleteView.as_view(), name='cliente_delete'),
    path('cliente-detail/<int:pk>/', ClienteDetailView.as_view(), name='cliente_detail'),
    path('cliente-update/<int:pk>/', ClienteUpdateView.as_view(), name='cliente_update'),

]
