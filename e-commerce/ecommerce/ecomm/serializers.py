from .models import Customer,Order,OrderItem
from rest_framework import serializers

class CustomerSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(max_length=200, min_length=3, allow_blank=False,trim_whitespace=True)
    address = serializers.CharField(max_length=200, min_length=10, allow_blank=False, trim_whitespace=True)
    class Meta:
        model = Customer
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    customer = (serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all()))
    customer_details = (CustomerSerializer(source='customer',read_only=True))
    class Meta:
        model = Order
        fields = ['customer', 'customer_details', 'order_date']

class OrderItemSerializer(serializers.ModelSerializer):
    order = (serializers.PrimaryKeyRelatedField(queryset=Order.objects.all()))
    order_details = (OrderSerializer(source='order', read_only=True))
    class Meta:
        model = OrderItem
        fields = ['order', 'order_details', 'item_name', 'quantity']
