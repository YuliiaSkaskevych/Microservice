from .permissions import IsOwnerOrReadOnly
from rest_framework import viewsets
from .models import Order, OrderItem, OrderItemBookItem
from .serializers import OrderSerializer, OrderItemSerializer, OrderItemBookItemSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsOwnerOrReadOnly]


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsOwnerOrReadOnly]


class OrderItemBookItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItemBookItem.objects.all()
    serializer_class = OrderItemBookItemSerializer
    permission_classes = [IsOwnerOrReadOnly]
