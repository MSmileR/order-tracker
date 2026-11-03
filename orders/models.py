from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True,)
    notes = models.CharField(max_length=200, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES = [
        ("new", "New"),
        ("in_production", "In production"),
        ("packed", "Packed"),
        ("shipped", "Shipped"),
    ]
    shopify_order_id = models.CharField(max_length=100, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    order_date = models.DateField()
    deadline = models.DateField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    materials_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    notes = models.TextField(blank=True)

    @property
    def profit(self):
        return self.price - self.materials_cost

    def __str__(self):
        return f"Order for {self.customer.name} on {self.order_date}"