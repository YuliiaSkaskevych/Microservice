from django.urls import path, include

from .views import RegisterFormView, UpdateProfile, UserProfile

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', RegisterFormView.as_view(), name='register'),
    path("update_profile/", UpdateProfile.as_view(), name='update_profile'),
    path("my_profile/", UserProfile.as_view(), name="profile"),
]
