from django.urls import include, path
from rest_framework import routers
from stock import views

router = routers.DefaultRouter()
router.register(r'author', views.AuthorViewSet)
router.register(r'book', views.AuthorViewSet)
router.register(r'instance', views.BookInstanceViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    ]
