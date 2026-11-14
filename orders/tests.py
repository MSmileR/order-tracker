from django.test import TestCase
from .models import Order
from decimal import Decimal

# Create your tests here.

class OrderProfitTest(TestCase):
    def test_profit_is_price_minus_materials_cost(self):
        order = Order(
            price=Decimal('500.00'),
            materials_cost=Decimal('3.00')
        )
        self.assertEqual(order.profit, Decimal('497.00'))

    def test_profit_can_be_negative(self):
        order = Order(
            price=Decimal('100.00'),
            materials_cost=Decimal('120.00')
        )
        self.assertEqual(order.profit, Decimal('-20.00'))