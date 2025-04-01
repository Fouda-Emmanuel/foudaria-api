from django.urls import path
from . import views
from .views import  OrderUpdateView, OrderDeleteView

urlpatterns =[
    path('', views.OrderListView.as_view(), name='orders'),
    path('my-orders/', views.MyOrderList.as_view(), name='my_orders'),
    path('create/', views.OrderCreateView.as_view(), name='create_order'),
    path('car-prices/', views.CarListView.as_view(), name='create_order'),
    path('details/<lookup_value>/', views.OrderDetailView.as_view(), name='order_details'),
    # path('customer/<int:user_id>/<lookup_value>/', views.OrderDetailView.as_view(), name='order_details'),
    path('update/<lookup_value>/', OrderUpdateView.as_view(), name='order_update'),
    path('delete/<lookup_value>/', OrderDeleteView.as_view(), name='order_delete'),

    #payment endpoints
#     path("paypal/create/", PayPalPaymentView.as_view(), name="paypal_create"),
#     path("paypal/success/", PayPalSuccessView.as_view(), name="paypal_success"),
#     path("paypal/cancel/", PayPalCancelView.as_view(), name="paypal_cancel"),
] 

