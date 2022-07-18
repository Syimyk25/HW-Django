from django.urls import path
from applications.product.views import ProductListCreateView, ProductRetrieveUpdateDestroyView

urlpatterns = [
    path('', ProductListCreateView.as_view()),
    path('<int:pk>/', ProductRetrieveUpdateDestroyView.as_view()),
]