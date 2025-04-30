from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Product


class ProductAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.valid_payload = {"product_name": "Laptop", "price": 1200, "quantity": 50}
        self.invalid_payloads = [
            {"product_name": "", "price": 100, "quantity": 10},  # Empty name
            {
                "product_name": "Mouse",
                "price": "not-a-number",
                "quantity": 10,
            },  # Invalid price
            {
                "product_name": "Keyboard",
                "price": 30,
                "quantity": "lots",
            },  # Invalid quantity
            {"price": 30, "quantity": 10},  # Missing product_name
            {"product_name": "Monitor", "quantity": 10},  # Missing price
            {"product_name": "Monitor", "price": 300},  # Missing quantity
        ]

    def test_create_product_success(self):
        response = self.client.post("/api/products/", self.valid_payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().product_name, "Laptop")

    def test_create_product_failure(self):
        for payload in self.invalid_payloads:
            response = self.client.post("/api/products/", payload, format="json")
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_read_products(self):
        # Prepopulate products
        Product.objects.create(product_name="Laptop", price=1200, quantity=50)
        Product.objects.create(product_name="Mouse", price=25, quantity=200)

        response = self.client.get("/api/products/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()
        self.assertEqual(len(data), 2)
        self.assertIn("1", data)
        self.assertEqual(data["1"]["product_name"], "Laptop")
