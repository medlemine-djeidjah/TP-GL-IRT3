from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

from .models import CarPart, Order ,OrderItem
import json


def car_parts_store(request):
    return render(request, 'store.html')

def car_parts_store_api(request):
    parts = CarPart.objects.all().values('id', 'name', 'description', 'price', 'image_url')
    return JsonResponse(list(parts), safe=False)

def shop_cart(request):
    return render(request, 'cart.html')


def checkout(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            cart_data = data.get('cart', [])
            total_amount = data.get('totalAmount', 0)

            if not cart_data:
                return JsonResponse({'error': 'Cart is empty or not properly formatted'}, status=400)

            # Create the order without total_price initially
            order = Order.objects.create(order_number="123")  # Add your order_number logic here

            # Create OrderItem instances
            for item_data in cart_data:
                part_id = item_data['id']  # Assuming the 'id' field corresponds to the CarPart ID
                quantity = item_data['quantity']
                part = CarPart.objects.get(pk=part_id)
                total_price = part.price * quantity

                OrderItem.objects.create(
                    order=order,
                    part=part,
                    quantity=quantity,
                    total_price=total_price
                )

            # Update the total_price of the order
            order.update_total_price()

            return JsonResponse({'message': 'Order created successfully!'})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
        except CarPart.DoesNotExist:
            return JsonResponse({'error': 'One or more items in the cart do not exist'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)