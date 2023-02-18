from django.urls import path
from . import views

app_name = 'concept_map'

urlpatterns = [
    path('', views.NodeListView.as_view(), name='node_list'),
    path('nodes/<int:pk>/', views.NodeDetailView.as_view(), name='node_detail'),
    path('nodes/new/', views.NodeCreateView.as_view(), name='node_create'),
    path('connections/new/', views.ConnectionCreateView.as_view(), name='connection_create'),
]