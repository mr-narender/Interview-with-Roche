from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer


class ProductAPIView(APIView):
    def get(self, request, id=None):
        if id:
            try:
                product = Product.objects.get(id=id)
                data = {
                    str(product.id): {
                        "product_name": product.product_name,
                        "price": float(product.price),
                        "quantity": product.quantity,
                    }
                }
                return Response(data, status=status.HTTP_200_OK)
            except Product.DoesNotExist:
                return Response(
                    {"detail": "Product not found."}, status=status.HTTP_404_NOT_FOUND
                )
        else:
            # No id provided, return all products
            products = Product.objects.all()
            data = {
                str(product.id): {
                    "product_name": product.product_name,
                    "price": float(product.price),
                    "quantity": product.quantity,
                }
                for product in products
            }
            return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Product created."}, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
