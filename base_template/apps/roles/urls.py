from django.urls import path
from .views import RoleListCreateView, RoleDetailView

urlpatterns = [
    path('', RoleListCreateView.as_view(), name='role_list_create'),
    path('<int:pk>/', RoleDetailView.as_view(), name='role_detail'),
]