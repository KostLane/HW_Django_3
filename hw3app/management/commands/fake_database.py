from django.core.management.base import BaseCommand
from hw3app.models import Client, Product, Order
import time

class Command(BaseCommand):
    help = 'FAKE DB'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='COUNT CLIENTS')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        products = []
        for j in range(1, count + 1):
            product = Product(
                name=f'Товар_{j}',
                description=f'Описание товара_{j}',
                price=j*6,
                quantity=j*10
            )
            product.save()
            products.append(product)

        for i in range(1, count + 1):
            client = Client(
                name=f'Клиент{i}',
                email=f'example{i}_{time.time()}@mail.ru',
                phone=f'+7(978)000-11-{i*2}',
                address=f'Адресс_{i}'
            )
            client.save()
            for product in products:
                order = Order(client=client, quantity=j, total_price=product.price * j)
                order.save()
                order.product.add(product)

        self.stdout.write(f'DB READY!!!')