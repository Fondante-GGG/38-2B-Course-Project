from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView

from .forms import RegisterForm

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("login")

class LoginView(LoginView):
    template_name = "accounts/login.html"

class LogoutView(LogoutView):
    next_page = reverse_lazy("login")