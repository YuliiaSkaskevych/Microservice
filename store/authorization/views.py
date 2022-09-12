from django.shortcuts import render

from django.contrib.auth import get_user_model, authenticate, login
from django.urls import reverse_lazy
from django.views import generic

from .forms import RegistrationForm, RegisterForm

from django.views.generic import CreateView, DetailView, UpdateView

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin


User = get_user_model()


def home(request):
    return render(request, 'index.html')


class RegisterFormView(generic.FormView):
    template_name = 'authorization/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        user = form.save()
        user = authenticate(username=user.username, password=form.cleaned_data.get("password1"))
        login(self.request, user)
        return super(RegisterFormView, self).form_valid(form)


class UpdateProfile(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = User
    fields = ['username', "first_name", "last_name", "email"]
    template_name = 'authorization/update_profile.html'
    success_url = reverse_lazy("profile")
    success_message = "Profile updated successfully!"

    def get_object(self, queryset=None):
        user = self.request.user
        return user


class UserProfile(LoginRequiredMixin, generic.DetailView):
    model = User
    template_name = "authorization/profile.html"

    def get_object(self, queryset=None):
        user = self.request.user
        return user
