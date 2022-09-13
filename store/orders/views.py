from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from django.contrib import messages


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         book=item['book'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            messages.add_message(request, messages.SUCCESS, 'Order was created successfully!')
            cart.clear()
            return render(request, 'orders/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'orders/create.html',
                  {'cart': cart, 'form': form})


class OrderListView(LoginRequiredMixin, generic.ListView):
    model = Order
    paginate_by = 5
    template_name = 'orders/orders_list.html'


def user_order(request, pk):
    """Information about entered book: author, store, publisher"""
    orderitem = OrderItem.objects.select_related('order').get(order_id=pk)
    return render(
        request,
        'orders/user_order.html',
        {"orderitem": orderitem})


class OrderDeleteView(LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    model = Order
    template_name = 'orders/delete_order.html'
    success_message = "Order was canceled successfully!"
    success_url = reverse_lazy('my_orders')


class OrderUpdateView(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = Order
    fields = ['first_name', 'last_name', 'email', 'address', 'city']
    template_name = 'orders/update_order.html'
    success_message = "Order was update successfully!"
    success_url = reverse_lazy('my_orders')
