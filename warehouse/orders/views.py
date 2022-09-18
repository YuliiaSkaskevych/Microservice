from stock.models import Book
from .permissions import IsOwnerOrReadOnly
from rest_framework import viewsets
from .models import Order, OrderItem, OrderItemBookItem
from .serializers import OrderSerializer, OrderItemSerializer, OrderItemBookItemSerializer, GetRequestSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser


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


@api_view(['POST'])
def get_request(request):
    data = JSONParser().parse(request)
    serializer = GetRequestSerializer(data=data)
    if serializer.is_valid():
        queryset = Book.objects.filter(title=serializer.data['title'])
        queryset[0].delete()
        return JsonResponse(serializer.data, status=201)
    else:
        return JsonResponse(serializer.errors, status=400)
