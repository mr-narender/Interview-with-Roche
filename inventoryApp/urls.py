from django.urls import path
from .views import ProductAPIView

urlpatterns = [
    path(
        "products/", ProductAPIView.as_view(), name="product-list"
    ),  # For listing all products
    path(
        "products/<int:id>/", ProductAPIView.as_view(), name="product-detail"
    ),  # For fetching a product by id
]
