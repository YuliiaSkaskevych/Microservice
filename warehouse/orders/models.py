from django.db import models
from stock.models import Book, BookItem


class Order(models.Model):
    IN_PROGRESS = 'In_progress'
    PACKED = 'Packed'
    DELIVERING = 'Delivering'
    RECEIVED = 'Received'

    CHOICE_STATUS = {
        (IN_PROGRESS, 'In_progress'),
        (PACKED, 'Packed'),
        (DELIVERING, 'Delivering'),
        (RECEIVED, 'Received')
    }

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    status = models.CharField('Status', choices=CHOICE_STATUS, max_length=30, default=IN_PROGRESS)
    order_id_in_shop = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return 'Order {}'.format(self.pk)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.order

    def get_cost(self):
        return f'{self.price} * {self.quantity}'


class OrderItemBookItem(models.Model):
    order_item_id = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    book_item_id = models.ForeignKey(BookItem, on_delete=models.CASCADE)
