from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from . models import *
# Create your views here.
def index(request):
    testtimonials = Testimonials.objects.all()
    context = {'testimonials': testtimonials}
    return render(request, 'index.html')

def homes(request):
    homes = Upload.objects.all()
    title = 'Zillian Homes'
    return render(request, 'homes/homes.html', {'homes':homes, 'title': title})

def contact_us(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def home_single(request, pk):
    home = Upload.objects.filter(id=pk)
    context = {'home': home}
    return render(request, 'homes/listings_single.html', context)

def search(request):
    try:
        if request.method == 'GET':
            type = request.GET.get('type')
            category = request.GET.get('category')
            bedroom = request.GET.get('bedrooms')
            min_price = request.GET.get('min_price')
            min = min_price.replace(',', '')
            max_price = request.GET.get('max_price')
            max = max_price.replace(',', '')
            homes = Upload.objects.filter(bedrooms__icontains=bedroom, type__icontains=type,
                                        category__icontains=category, price__range=(min, max))
            title = 'Search Properties'
    except Exception as e:
        print(e)
        return HttpResponse('<h1>Error!!! please input correct search options</h1>')
    return render(request, 'homes/homes.html', {'homes': homes, 'title': title})

def subscriber(request):
    if request.method == 'POST':    
        email = request.POST.get('email', False)
        subscriber = Subscriber(email=email)
        subscriber.save()
        return redirect('/')
    else:
        return render(request, 'index.html')