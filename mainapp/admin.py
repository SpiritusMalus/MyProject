from django.contrib import admin

from basketapp.models import Basket
from mainapp.models import User, Product


class BasketAdmin(admin.ModelAdmin):
    pass


admin.site.register(Basket, BasketAdmin)


class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)


class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)
