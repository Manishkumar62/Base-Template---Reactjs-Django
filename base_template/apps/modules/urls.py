from django.urls import path
from .views import ModuleListCreateView, ModuleDetailView, UserMenuView

urlpatterns = [
    path('', ModuleListCreateView.as_view(), name='module_list_create'),
    path('my-menu/', UserMenuView.as_view(), name='user_menu'),
    path('<int:pk>/', ModuleDetailView.as_view(), name='module_detail'),
]