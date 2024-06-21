import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projectBE.settings')
django.setup()

from ecommerce.models import Item, Customer, Order, OrderItem, ShippingAddress

def view_items():
    items = Item.objects.all()
    for item in items:
        print(f"Item Name: {item.name}, Description: {item.description}, Price: {item.price}")

def view_customers():
    customers = Customer.objects.all()
    for customer in customers:
        print(f"Customer Name: {customer.name}, User: {customer.user}")

def view_orders():
    orders = Order.objects.all()
    for order in orders:
        print(f"Order ID: {order.id}, Customer: {order.customer}, Date Ordered: {order.date_ordered}, Complete: {order.complete}, Transaction ID: {order.transaction_id}")

def view_order_items():
    order_items = OrderItem.objects.all()
    for item in order_items:
        print(f"Order Item: {item.product.name}, Quantity: {item.quantity}, Order ID: {item.order.id}")

def view_shipping_addresses():
    shipping_addresses = ShippingAddress.objects.all()
    for address in shipping_addresses:
        print(f"Address: {address.address}, City: {address.city}, State: {address.state}, Zipcode: {address.zipcode}, Customer: {address.customer}, Order: {address.order}")

if __name__ == "__main__":
    print("Viewing Items:")
    view_items()
    print("\nViewing Customers:")
    view_customers()
    print("\nViewing Orders:")
    view_orders()
    print("\nViewing Order Items:")
    view_order_items()
    print("\nViewing Shipping Addresses:")
    view_shipping_addresses()
