from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status, permissions
from rest_framework.views import APIView
from paypalrestsdk.payments import Payment
from .paypal import get_paypal_client
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from .models import Order, User
from .serializers import OrderSerializer, CarListSerializer
from .permission import CustomIsAdmin
from .constant import CAR_PRICES
from drf_yasg.utils import swagger_auto_schema


# Create your views here.
class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(operation_summary="List All Orders")
    def get(self, request, *args, **kwargs):
        serializer = OrderSerializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)    
    
    
class MyOrderList(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(operation_summary="List Your Own Orders")
    def get(self, request):
        serializer = OrderSerializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def get_queryset(self):
        return Order.objects.filter(customer= self.request.user) 
    

class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(operation_summary="Create an Order")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
   
    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)


class CarListView(APIView):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(operation_summary="View all Cars and Prices")
    def get(self, request):
        cars = [{"name": name, "price": price} for name, price in CAR_PRICES.items()]
        serializer = CarListSerializer(cars, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    
class OrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [CustomIsAdmin]

    @swagger_auto_schema(operation_summary="View a particular Order")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    def get_object(self):
        lookup_value = self.kwargs.get("lookup_value")  
        if lookup_value.isdigit():  
            return get_object_or_404(Order, pk=int(lookup_value))
        else:  
            return get_object_or_404(Order, order_id=lookup_value)
        

# class UserOrderDetailView(generics.GenericAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer

#     def get(self, user_id):
#         user = User.objects.get(id=user_id)  # Get user ID from URL

#         order = Order.objects.all().filter(customer=user)
#         serializer = OrderSerializer(order, many=True)

#         return Response(serializer.data, status=status.HTTP_200_OK)


class OrderUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(operation_summary="Update an Order")
    def get_object(self):
        lookup_value = self.kwargs.get("lookup_value")  
        if lookup_value.isdigit():  
            return get_object_or_404(Order, pk=int(lookup_value))
        else:  
            return get_object_or_404(Order, order_id=lookup_value)
    
    def perform_update(self, serializer):
        order = self.get_object()
        user = self.request.user
        
        if user.is_superuser or order.customer == user:
            serializer.save()
        else:
            raise PermissionDenied("You do not have permission to update this order.")
   
    

class OrderDeleteView(generics.RetrieveDestroyAPIView):
    
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    @swagger_auto_schema(operation_summary="Delete an Order")
    def get_object(self):
        lookup_value = self.kwargs.get("lookup_value")  
        if lookup_value.isdigit():  
            return get_object_or_404(Order, pk=int(lookup_value))
        else:  
            return get_object_or_404(Order, order_id=lookup_value)
    
    def perform_destroy(self, instance):
        user = self.request.user

        if user.is_superuser or instance.customer == user:
            instance.delete()
        else:
            raise PermissionDenied("You do not have permission to delete this order.")
    





# class PayPalPaymentView(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def post(self, request, *args, **kwargs):
#         paypal = get_paypal_client()
#         order_id = request.data.get("order_id")
#         order = get_object_or_404(Order, order_id=order_id, customer=request.user)

#         payment = Payment({
#             "intent": "sale",
#             "payer": {"payment_method": "paypal"},
#             "redirect_urls": {
#                 "return_url": "http://localhost:8000/orders/paypal/success/",
#                 "cancel_url": "http://localhost:8000/orders/paypal/cancel/"
#             },
#             "transactions": [{
#                 "item_list": {
#                     "items": [{
#                         "name": order.car,
#                         "sku": str(order.order_id),  # Fix SKU to store order ID
#                         "price": str(order.price),
#                         "currency": "USD",
#                         "quantity": order.quantity
#                     }]
#                 },
#                 "amount": {"total": str(order.price), "currency": "USD"},
#                 "description": f"Payment for Order {order.order_id}"
#             }]
#         })

#         if payment.create():
#             for link in payment.links:
#                 if link.rel == "approval_url":
#                     return Response({"payment_url": link.href})
#         else:
#             return Response({"error": payment.error}, status=400)

       

# class PayPalSuccessView(APIView):
#     def get(self, request, *args, **kwargs):
#         payment_id = request.GET.get("paymentId")
#         payer_id = request.GET.get("PayerID")

#         payment = Payment.find(payment_id)
#         if payment.execute({"payer_id": payer_id}):
#             # Update order status to paid
#             order_id = payment.transactions[0].item_list.items[0].sku  # Assuming SKU is order ID
#             order = Order.objects.get(order_id=order_id)
#             order.payment_status = "Completed"
#             order.payment_method = 'PayPal'
#             order.save()
#             return Response({"message": "Payment successful"})
#         else:
#             return Response({"error": payment.error}, status=status.HTTP_400_BAD_REQUEST)

# class PayPalCancelView(APIView):
#     def get(self, request, *args, **kwargs):
#         return Response({"message": "Payment cancelled"})


    
