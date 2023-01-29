from django.urls import path, include

from .views import *



urlpatterns = [
    path('', basket, name='view'),
    path('basket_adding/', basket_adding, name='basket_adding'),
    path('basket_remove/', basket_remove, name='basket_remove'),
    path('basket_quantity/', basket_quantity, name='basket_quantity'),
]
