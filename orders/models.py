import uuid
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()

class Order(models.Model):
    ORDER_STATUS = (
        ('Pending', 'Pending'),
        ('In_Transit', 'In_Transit'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    )

    PAYMENT_STATUS = (
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Failed', 'Failed'),
    )

    PAYMENT_METHODS = (
        ('PayPal', 'PayPal'),
        ('CinetPay', 'CinetPay'),
        ('Stripe', 'Stripe'),
    )

    CAR_PRICES = {
        'Aston Martin DBX': 2000,
        'Range Rover': 1500,
        'Lamborghini Urus': 3500,
        'Ferrari SF90': 3000,
        'Tesla Cybertruck': 1200,
        'Rolls-Royce Cullinan': 3500,
        'Porsche 911 Turbo S': 2500,
        'Bugatti Veyron': 5000,
        'Bentley Bentayga': 2200,
        'Mercedes G-Wagon': 1800,
    }

    CARS = [(car, car) for car in CAR_PRICES.keys()]

    order_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    car = models.CharField(max_length=100, choices=CARS, default='Aston Martin DBX')
    quantity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)])
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, editable=False)
    order_status = models.CharField(max_length=50, choices=ORDER_STATUS, default='Pending')
    payment_status = models.CharField(max_length=50, choices=PAYMENT_STATUS, default='Pending')
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHODS, default='PayPal')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        """ Automatically calculate price before saving. """
        self.price = self.CAR_PRICES[self.car] * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Order {self.order_id} | {self.car} x{self.quantity} | {self.customer.username} | ${self.price}'
