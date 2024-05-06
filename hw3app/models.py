from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=120)
    date_registr = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Клиент: {self.name}, Эл.почта: {self.email}, Адресс: {self.address}'
    
class Product(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    data_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Товар: {self.name}, Цена: {self.price}'
    
class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    data_ordered = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return f'Заказ: {self.client}, Сумма заказа: {self.total_price}'