from django.db.models import Count
from django.shortcuts import render, redirect
from orders.models import OrderProduct
from slider.models import Slider
from store.models import Product, ReviewRating


def home(request):
    # Get photos for slider
    slider_list = Slider.objects.all()

    # Get most popular products
    filtered_products = (OrderProduct.objects.values('product_id').
                         annotate(product_count=Count('product_id')).
                         order_by('-product_count')[:8])

    most_popular_products = [Product.objects.get(id=product['product_id']) for product in filtered_products]

    # Get the reviews
    reviews = None
    for product in most_popular_products:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)

    context = {
        'most_popular_products': most_popular_products,
        'reviews': reviews,
        'slider_list': slider_list
    }
    return render(request, 'home.html', context)


# Добавьте эти новые функции представления
def privacy_policy(request):
    context = {
        'title': 'Политика конфиденциальности'
    }
    return render(request, 'privacy_policy.html', context)

def terms_of_use(request):
    context = {
        'title': 'Условия использования'
    }
    return render(request, 'terms_of_use.html', context)

def shipping_payment(request):
    context = {
        'title': 'Доставка и оплата'
    }
    return render(request, 'shipping_payment.html', context)

def returns(request):
    context = {
        'title': 'Возврат товара'
    }
    return render(request, 'returns.html', context)