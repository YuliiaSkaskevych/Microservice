from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.views import generic
from .tasks import send_mail_to_admin, send_mail_to_owner
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
            text = f'Order {order.pk} was created by {order.owner}'
            text1 = f'Your order {order.pk} was created successfully!'
            send_mail_to_admin.delay(text, order.email)
            send_mail_to_owner.delay(text1, order.email)
            cart.clear()
            return render(request, 'orders/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'orders/create.html',
                  {'cart': cart, 'form': form})


class OrderListView(PermissionRequiredMixin, generic.ListView):
    model = Order
    permission_required = 'can_mark_returned'
    paginate_by = 5
    template_name = 'orders/orders_list.html'


def user_order(request, pk):
    """Information about entered book: author, store, publisher"""
    orderitem = OrderItem.objects.select_related('order').get(order_id=pk)
    return render(
        request,
        'orders/user_order.html',
        {"orderitem": orderitem})
