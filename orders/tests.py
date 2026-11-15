from datetime import date

from django.contrib.auth.models import User
from django.urls import reverse


from django.test import TestCase
from .models import Customer, Order
from decimal import Decimal

# Create your tests here.
class OrderListViewTest(TestCase):
    def test_redirects_to_login_when_not_logged_in(self):
        response = self.client.get(reverse('order_list'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/admin/login/', response.url)

    def test_shows_orders_when_logged_in(self):
        user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

        customer = Customer.objects.create(name='Test Customer')
        Order.objects.create(
            shopify_order_id='#T1',
            customer=customer,
            order_date=date.today(),
            price=Decimal('100.00'),
        )
        response = self.client.get(reverse('order_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '#T1')


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