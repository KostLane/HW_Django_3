from django.shortcuts import render, get_object_or_404
from datetime import timedelta
from .models import Client, Product, Order
import django.utils.timezone
 
# Create your views here.

def index(request):
    
    html = """
    <h1>Главная страница</h1>
    <p>Задание №3:</p>
    <p>Создайте шаблон, который выводит список заказанных клиентом товаров из всех его заказов с сортировкой по времени:</p>
    <p>— за последние 7 дней (неделю)</p>
    <p>— за последние 30 дней (месяц)</p>
    <p>— за последние 365 дней (год)</p>
    <p>Товары в списке не должны повторятся.</p>
    """
    title = "Задание №3"
    return render(request, 'hw3app/index.html', {'html': html, 'title': title})

def client_orders(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(client=client)
    request.session['client_id'] = client_id

    now = django.utils.timezone.now()

    products_by_time = {
        'week': set(),
        'month': set(),
        'year': set(),
        'count_orders_week': 0,
        'count_orders_month': 0,
        'count_orders_year': 0,
        'sum_orders_week': 0,
        'sum_orders_month': 0,
        'sum_orders_year': 0,
    }

    for order in orders:
        products = Product.objects.filter(order=order)

        for product in products:
            if order.data_ordered >= now - timedelta(days=7):
                products_by_time['week'].add(product)
                products_by_time['count_orders_week'] += 1
                products_by_time['sum_orders_week'] += order.total_price * order.quantity
            elif order.data_ordered >= now - timedelta(days=30):
                products_by_time['month'].add(product)
                products_by_time['count_orders_month'] += 1
                products_by_time['sum_orders_month'] += order.total_price * order.quantity
            elif order.data_ordered >= now - timedelta(days=365):
                products_by_time['year'].add(product)
                products_by_time['count_orders_year'] += 1
                products_by_time['sum_orders_year'] += order.total_price * order.quantity

    return render(request, 'hw3app/client_orders.html', {'client': client, 'products_by_time': products_by_time, 'orders': orders})