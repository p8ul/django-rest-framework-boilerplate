from django.urls import path
from .views import (
   ModuleCreateAPIView,
   ModuleListAPIView,
   ModuleDeleteAPIView,
   ModuleDetailAPIView,
   ModuleUpdateAPIView
)

urlpatterns = [
    path('', ModuleListAPIView.as_view(), name='list'),
    path('create', ModuleCreateAPIView.as_view(), name='create'),
    path('delete/<int:pk>/', ModuleDeleteAPIView.as_view(), name='delete'),
    path('detail/<int:pk>/', ModuleDetailAPIView.as_view(), name='detail'),
    path('update/<int:pk>/', ModuleUpdateAPIView.as_view(), name='update')
]
