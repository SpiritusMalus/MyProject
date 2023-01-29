from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, FormView

from basketapp.models import Basket
from .forms import MyUserCreationForm, AuthUserForm
from .models import *


class Main(ListView, FormView):
    template_name = 'mainapp/index.html'

    def get(self, request):
        basket = Basket.objects.all()
        quantity = 0
        for i in basket:
            quantity += i.quantity
        context = {
            "context": Product.objects.all(),
            "basket": basket,
            "AuthUserForm": AuthUserForm,
            'users': User.objects.all(),
            'quantity': quantity,
        }

        return render(request, "mainapp/products.html", context)

    def post(self, request, *args, **kwargs):
        # form = AuthUserForm(request.POST)
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            # Auth
            user = authenticate(request, username=username, password=password)
            # login - continue session
            login(request, user)

            return redirect('main')

        context = {
            "context": Product.objects.all(),
            "basket": Basket.objects.all(),
            'AuthUserForm': AuthUserForm(data=request.POST),
            'users': User.objects.all(),

        }
        return render(request, "mainapp/products.html", context)

    # def get_context_data(self, **kwargs):
    #     context = {
    #         "context": Product.objects.all(),
    #         "AuthUser": AuthUser,
    #     }
    #     return context


class Registration(CreateView):
    form_class = MyUserCreationForm
    template_name = 'mainapp/register.html'
    success_url = reverse_lazy('main')

    # def get_context_data(self):
    #     context = {
    #         "context": Product.objects.all(),
    #         "AuthUser": AuthUser,
    #     }
    #     return render(request, "mainapp/products.html", context)
