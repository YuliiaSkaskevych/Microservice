from django.urls import path

from . import views
from .views import OrderListView, UserOrder

urlpatterns = [
    path('create_order/', views.order_create, name='order_create'),
    path('my_orders/', OrderListView.as_view(), name='my_orders'),
    path('my_orders/<int:pk>', UserOrder.as_view(), name='user_order'),
]
