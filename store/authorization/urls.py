from django.urls import path, include

from .views import RegisterFormView, UpdateProfile


urlpatterns = [
    path('register/', RegisterFormView.as_view(), name='register'),
    path('profile/edit/', UpdateProfile.as_view(), name='user_update'),
    path('accounts/', include('django.contrib.auth.urls')),
]
