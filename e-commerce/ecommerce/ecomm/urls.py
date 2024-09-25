from django.contrib import admin
from django.urls import path
from .views import customer_list, customer_list_view,order_list,order_list_view,orderitem_list,orderitem_list_view

urlpatterns = [
    path('customer', customer_list),
    path('customers/<int:passed_id>', customer_list_view),
    path('order', order_list),
    path('orders/<int:passed_id>', order_list_view),
    path('orderitem', orderitem_list),
    path('orderitems/<int:passed_id>', orderitem_list_view)
]