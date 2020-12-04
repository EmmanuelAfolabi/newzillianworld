from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import *
from .form import CreateUserForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from decimal import Decimal as D
from django import forms
from django.views.generic.edit import FormView
#from .form import FileFieldForm
from django.forms import modelformset_factory
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, DetailView
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
#from django.core.mmail import send_mail, BadHeaderError
import json
import datetime
from .utils import cookiebag, bagData, guestOrder
from .form import DocumentForm
from homes.models import Subscriber





# Create your views here.
def aquarium(request):
    data = bagData(request)
    bagItemsA = data['bagItemsA']

    products = Product.objects.all()
    context = {'products': products, 'bagItemsA': bagItemsA}
    return render(request, 'aquarium/aquarium.html', context)

def aquarium_single(request, pk):
    try:
        data = bagData(request)
        bagItemsA = data['bagItemsA']
        order = data['order']
        items = data['items']

        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            comment = request.POST['comment']
            products = Product.objects.get(id=pk)

            reply = Reply(product=products, name=name, email=email, comment=comment,)
            reply.save()
            return redirect('aquarium')
    except Exception as e:
        return HttpResponse('<h1>Error!!! </h1>')

    products = Product.objects.filter(id=pk)
    id = Product.objects.get(id=pk)
    comments = Reply.objects.filter(product=pk)
    context = {'products': products, 'items': items, 'order': order, 'bagItemsA': bagItemsA, 'comments': comments}
    return render(request, 'aquarium/aquarium_single.html', context)


def aquarium_bag(request):
    data = bagData(request)
    bagItemsA = data['bagItemsA']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'bagItemsA': bagItemsA}
    return render(request, 'aquarium/cart.html', context)

def aquarium_checkout(request):
    data = bagData(request)
    bagItemsA = data['bagItemsA']
    order = data['order']
    items = data['items']

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print('Valid form')
            return redirect('aquarium')

    else:
        form = DocumentForm()
        print('Invalid form')
        
    context = {'items': items, 'order': order, 'bagItemsA': bagItemsA, 'form': form}
    return render(request, 'aquarium/checkout.html', context)


def aquarium_updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('Item was added', safe=False)


def aquarium_processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

    else:
        customer, order = guestOrder(request, data)

    total = str(data['form']['total'])
    order.transaction_id = transaction_id

    if total == float(order.get_bag_total):
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            streetaddress=data['shipping']['streetAddress'],
            apartmentaddress=data['shipping']['apartmentAddress'],
            town=data['shipping']['town'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],
            code=data['shipping']['code'],
            subtotal=data['shipping']['subtotal'],
            total=data['shipping']['total'],

        )
        #customer, order = guestOrder(request, data)

    return JsonResponse('Payment submitted..', safe=False)



def search(request):
    try:
        data = bagData(request)
        bagItemsA = data['bagItemsA']

        if request.method == 'GET':
            name = request.GET.get('name')
            search = Product.objects.filter(name__icontains=name,)
    except Exception as e:
        return HttpResponse('<h1>Error!!! please input correct search options</h1>')
    context = {'bagItemsA': bagItemsA, 'search': search}
    return render(request, 'aquarium/search.html', context)

def subscriber(request):
    if request.method == 'POST':    
        email = request.POST.get('email', False)
        subscriber = Subscriber(email=email)
        subscriber.save()
        return redirect('aquarium')
    else:
        return render(request, 'aquarium/aquarium.html')





