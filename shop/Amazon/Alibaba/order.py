from django.shortcuts import render, redirect
from .models import Customer
from .views import View
from .products import Products
from .orders import Order
from django.contrib.auth.hashers import check_password
from alibaba.middlewares.auth import auth_middleware

class OrderView(View):
     def get(self, request):
          customer = request.session.get('customer')
          orders = Order.get_orders_by_customer(customer)
          print(orders)
          return render(request, 'orders,html', {'orders' : orders})
