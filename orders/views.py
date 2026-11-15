
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Order

# Create your views here.

class OrderListView(LoginRequiredMixin, generic.ListView):
    model = Order
    login_url = '/admin/login/'
    template_name = 'orders/order_list.html'
    context_object_name = 'orders'
    ordering = ['-order_date']