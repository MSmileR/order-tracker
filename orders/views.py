
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Order

# Create your views here.


class OrderDetailView(LoginRequiredMixin, generic.DetailView):
    model = Order
    login_url = '/admin/login/'
    template_name = 'orders/order_detail.html'

class OrderListView(LoginRequiredMixin, generic.ListView):
    model = Order
    login_url = '/admin/login/'
    template_name = 'orders/order_list.html'
    context_object_name = 'orders'
    ordering = ['-order_date']


    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.GET.get('status')
        if status:
            queryset = queryset.filter(status=status)
        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['statuses'] = Order.STATUS_CHOICES
        return context