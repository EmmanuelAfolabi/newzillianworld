from django.db import models
from django.conf import settings
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.shortcuts import reverse
# Create your models here.


choices = [
    ['Available', 'Available'],
    ['Sold Out', 'Sold Out'],
]

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, related_name='user_customer')
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=14, null=True)
    email = models.EmailField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping

class Product(models.Model):
    name = models.CharField(max_length=150, null=True)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=5000, blank=True)
    availability = models.CharField(choices=choices, max_length=20)
    digital = models.BooleanField(default=False, null=True, blank=False)
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    
    #category = models.CharField(choices=CATEGORY_CHOICES, null=False, max_length=30)
    #slug = models.SlugField()


    def __str__(self):
        return self.name

    @property
    def image1URL(self):
        try:
            url = self.image1.url
        except:
            url = ''
        return url

    @property
    def image2URL(self):
        try:
            url = self.image2.url
        except:
            url = ''
        return url

    @property
    def image3URL(self):
        try:
            url = self.image3.url
        except:
            url = ''
        return url

    def get_absolute_url(self):
        return reverse("product:detail", kwargs={
            'slug': self.slug
        })

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total\

    def __str__(self):
        return 'Order : ' + str(self.order), str(self.product), str(self.quantity)



class Receipt(models.Model):
    uniquecode = models.CharField(max_length=150, null=True)
    receipt =models.FileField(upload_to='media/', null=True)



class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    streetaddress = models.CharField(max_length=150, null=True)
    apartmentaddress = models.CharField(max_length=150, null=True)
    town = models.CharField(max_length=150, null=True)
    state = models.CharField(max_length=150, null=True)
    zipcode = models.CharField(max_length=150, null=True)
    code = models.CharField(max_length=14, null=True)
    subtotal =  models.CharField(max_length=150, null=True)
    total =  models.CharField(max_length=150, null=True)
    date_added = models.DateTimeField(auto_now_add=True)


class Reply(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=500, null=True)
    email = models.EmailField(max_length=500, null=True)
    comment = models.TextField(max_length=100000, null=True)
    date = models.DateField(auto_now_add=True, null=True)
    active = models.BooleanField(default=False, null=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return 'Comment {} by {}'.format(self.comment, self.name)