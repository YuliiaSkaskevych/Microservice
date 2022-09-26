from .models import Order, OrderItem, OrderItemBookItem
from rest_framework import serializers


class OrderItemSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = OrderItem
        fields = ['order', 'book', 'price', 'quantity']


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    order = serializers.ReadOnlyField(source='order.id')
    items = OrderItemSerializer(source="order_item_set", many=True)

    class Meta:
        model = Order
        fields = ['id', 'first_name', 'last_name', 'email', 'address', 'city', 'paid', 'created', 'updated']

    def create(self, validated_data):
        valid_data = validated_data.pop('order_item_set')
        order = Order.objects.create(**validated_data)
        order_items_serializer = self.fields['order_items']
        for each in valid_data:
            each['order'] = order
        order_items_serializer.create(valid_data)
        return order, valid_data


class OrderItemBookItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderItemBookItem
        fields = ["order_item_id", "book_item_id"]


class GetRequestSerializer(serializers.Serializer):
    title = serializers.CharField(required=True)
