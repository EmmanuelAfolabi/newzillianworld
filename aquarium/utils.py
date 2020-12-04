import json
from .models import *

def cookiebag(request):
    try:
        bag = json.loads(request.COOKIES['bag'])
    except:
        bag = {}
        print(bag)
    items = []
    order = {'get_bag_total': 0, 'get_bag_items': 0, "shipping": False}
    bagItemsA = order['get_bag_items']

    for i in bag:
        try:
            bagItemsA += bag[i]['quantity']

            product = Product.objects.get(id=i)
            total = (product.price * bag[i]['quantity'])

            order['get_bag_total'] += total
            order['get_bag_items'] += bag[i]['quantity']

            item = {
                'product': {
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'image1URL': product.image1URL,
                },
                'quantity': bag[i]['quantity'],
                'get_total': total,
            }
            items.append(item)

            if product.digital == False:
                order['shipping'] = True
        except:
            pass
    return {'bagItemsA': bagItemsA, 'order': order, 'items': items}

def bagData(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        bagItemsA = order.get_bag_items

    else:
        cookieData = cookiebag(request)
        bagItemsA = cookieData['bagItemsA']
        order = cookieData['order']
        items = cookieData['items']

    return {'bagItemsA': bagItemsA, 'order': order, 'items': items}

def guestOrder(request, data):
    print('User is not logged in..')
    print('COOKIES:', request.COOKIES)

    name = data['form']['name']
    phone = data['form']['phone']
    email = data['form']['email']

    cookieData = cookiebag(request)
    items = cookieData['items']

    customer, created = Customer.objects.get_or_create(
        phone=phone,
        email=email,
    )
    customer.name = name
    customer.save()

    order = Order.objects.create(
        customer=customer,
        complete=False,
    )

    for item in items:
        product = Product.objects.get(id=item['product']['id'])
        orderItem = OrderItem.objects.create(
            product=product,
            order=order,
            quantity=item['quantity']
        )
    return customer, order