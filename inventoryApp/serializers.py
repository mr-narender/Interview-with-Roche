from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["product_name", "price", "quantity"]

    def validate(self, data):
        errors = {}

        # Validate product_name
        product_name = data.get("product_name")
        if not product_name or not isinstance(product_name, str):
            errors["product_name"] = "This field is required and must be a string."

        # Validate price
        price = data.get("price")
        try:
            data["price"] = float(price)
        except (TypeError, ValueError):
            errors["price"] = "This field is required and must be a number."

        # Validate quantity
        quantity = data.get("quantity")
        try:
            data["quantity"] = int(quantity)
        except (TypeError, ValueError):
            errors["quantity"] = "This field is required and must be an integer."

        if errors:
            raise serializers.ValidationError(errors)

        return data
