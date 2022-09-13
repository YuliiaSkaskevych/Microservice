from django.urls import re_path, path
from . import views


urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('^add/(?P<book_id>\d+)/$', views.cart_add, name='cart_add'),
    path('^remove/(?P<book_id>\d+)/$', views.cart_remove, name='cart_remove'),
]
