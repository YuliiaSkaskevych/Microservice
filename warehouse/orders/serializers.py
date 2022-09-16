from .models import Order, OrderItem, OrderItemBookItem
from rest_framework import serializers


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    order = serializers.ReadOnlyField(source='order.id')

    class Meta:
        model = Order
        fields = ['id', 'first_name', 'last_name', 'email', 'address', 'city', 'paid', 'created', 'updated']


class OrderItemSerializer(serializers.HyperlinkedModelSerializer):
    order_item = serializers.ReadOnlyField(source='orderitem.order')

    class Meta:
        model = OrderItem
        fields = ['order', 'book', 'price', 'quantity']


class OrderItemBookItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderItemBookItem
        fields = ["order_item_id", "book_item_id"]
