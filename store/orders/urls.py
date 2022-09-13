from django.urls import path

from . import views
from .views import OrderListView, OrderDeleteView, OrderUpdateView

urlpatterns = [
    path('create_order/', views.order_create, name='order_create'),
    path('my_orders/', OrderListView.as_view(), name='my_orders'),
    path('my_orders/<int:pk>', views.user_order, name='user_order'),
    path('my_orders/<int:pk>/delete/', OrderDeleteView.as_view(), name='delete_order'),
    path('my_orders/<int:pk>/update/', OrderUpdateView.as_view(), name='update_order'),
]
