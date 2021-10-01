from django.urls import reverse_lazy
from .forms import SignupForm
from django.views.generic import CreateView
from django.http import HttpResponse


class SignUp(CreateView):
    """Sign up generic view"""
    form_class = SignupForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
