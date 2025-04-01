from rest_framework import serializers
from .models import Order
from django.contrib.auth import get_user_model

User = get_user_model() 

class OrderSerializer(serializers.ModelSerializer):
       customer = serializers.StringRelatedField(read_only=True) 
       order_status = serializers.CharField(read_only=True) 
       payment_status = serializers.CharField(read_only = True)
       price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
       
       class Meta:
            model = Order
            fields = ['customer', 'order_id', 'car', 'quantity', 'price', 'order_status', 'payment_status', 'payment_method','created_at', 'updated_at',]
            read_only_fields = ['order_id', 'price', 'created_at', 'updated_at', 'customer']
           


       def create(self, validated_data):
            request = self.context['request']
            validated_data['customer'] = request.user  
            return super().create(validated_data)
       
       
class CarListSerializer(serializers.Serializer):
      name = serializers.CharField()
      price = serializers.IntegerField()
