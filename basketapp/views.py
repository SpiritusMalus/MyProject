from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import Product, User
from django.views.generic import ListView, CreateView


def basket(request):
    basket = Basket.objects.all()
    quantity = 0
    for i in basket:
        quantity += i.quantity
    context = {
        "context": Product.objects.all(),
        'basket': basket,
        'quantity': quantity,
    }

    return render(request, 'basketapp/basket.html', context)


def basket_adding(request):
    session_key = request.session.session_key

    if not session_key:
        request.session.cycle_key()
    data = request.POST
    product_in_post = Product.objects.get(id=data['product_id'])
    # Ловлю Пост реквест, где все данные
    if data:
        # Тут я смотрю есть ли уже в БД добавленный продукт от юзера
        old_basket = Basket.objects.filter(product=product_in_post)
        # Если есть, то --
        if old_basket:
            product_id = old_basket[0].product.id
            # Сравниваю айди в баскете и айди в продукт(модель)
            if product_id == product_in_post.id:
                # Добавляю +1
                old_basket[0].quantity += 1
                old_basket[0].save()
        # Если нету ещё добавляем новый баскет в бд
        else:
            Basket.objects.create(session_key=session_key,
                                  user=User.objects.get(username=request.user),
                                  product=product_in_post,
                                  quantity=1)

    print(f'Session key: {request.session.session_key}')

    return render(request, 'basketapp/basket.html', locals())


def basket_remove(request):
    pk = request.POST['product_id']
    basket_record = get_object_or_404(Basket, pk=pk)
    basket_record.delete()
    return render(request, 'basketapp/basket.html', locals())


def basket_quantity(request):
    pk = request.POST['product_id']

    if request.POST['quantity_minus']:
        quantity_minus = request.POST['quantity_minus']
        basket_record = get_object_or_404(Basket, pk=pk)
        basket_record.quantity -= 1
        if basket_record.quantity == 0:
            basket_record.delete()
        basket_record.save()
    elif request.POST['quantity_plus']:
        quantity_plus = request.POST['quantity_plus']
        basket_record = get_object_or_404(Basket, pk=pk)
        basket_record.quantity += 1
    basket_total_price = basket_record.quantity * basket_record.price
    print(basket_total_price)
    return render(request, 'basketapp/basket.html', locals())
