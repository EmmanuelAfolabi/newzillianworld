from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


type = [
    ['Flat', 'Flat'],
    ['House', 'House'],
    ['Land', 'Land'],
    ['Commercial Property', 'Commercial Property']
]

availability = [
    ['Available', 'Available'],
    ['Rented', 'Rented'],
    ['Sold', 'Sold'],
]

category = [
    ['For Rent', 'For Rent'],
    ['For Sale', 'For Sale'],
    ['Joint Venture', 'Joint Venture'],
    ['Short Let', 'Short Let']
]

subtype = [
    ['Mini Flat', 'Mini Flat'],
    ['Self Contained(Single Rooms)', 'Self Contained(Single Rooms)'],
    ['Detached Bungalow', 'Mini Flat'],
    ['Detached Duplex', 'Detached Duplex'],
    ['Semi-detached Bungalow', 'Semi-detached Bungalow'],
    ['Semi-detached Duplex', 'Semi-detached Duplex'],
    ['Terraced Bungalow', 'Terraced Bungalow'],
    ['Terraced Duplex', 'Terraced Duplex'],
]

BEDROOM_CHOICES = {
    ('0', '0'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
}


class Upload(models.Model):
    title = models.CharField(max_length=100)
    availability = models.CharField(choices=availability, null=False, max_length=30)
    category = models.CharField(choices=category, null=False, max_length=30)
    type = models.CharField(choices=type, null=False, max_length=30)
    subtype = models.CharField(choices=subtype, null=False, max_length=30)
    locality = models.CharField(max_length=30, blank=True)
    street = models.CharField(max_length=30)
    description = models.TextField(max_length=5000)
    price = models.CharField(max_length=100)
    bedrooms = models.CharField(choices=BEDROOM_CHOICES, null=False, max_length=300, blank=True)
    toilets = models.CharField(choices=BEDROOM_CHOICES, null=False, max_length=30, blank=True)
    bathrooms = models.CharField(choices=BEDROOM_CHOICES, null=False, max_length=30, blank=True)
    parking = models.CharField(choices=BEDROOM_CHOICES, null=False, max_length=30, blank=True)
    toiletArea = models.CharField(max_length=300, blank=True)
    coveredArea = models.CharField(max_length=300, blank=True)
    videoLink = models.CharField(max_length=3000)
    image1 = models.FileField(upload_to='media/', null=True)
    image2 = models.FileField(upload_to='media/', null=True)
    image3 = models.FileField(upload_to='media/', null=True)
    image4 = models.FileField(upload_to='media/', null=True, blank=True)

    def __str__(self):
        return str(self.title)

class Testimonials(models.Model):
    message = models.TextField(max_length=5000)
    name = models.CharField(max_length=100)

class Feedbacks(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=5000)


class Subscriber(models.Model):
    email = models.EmailField(max_length=200)

class Reply(models.Model):
    Upload = models.ForeignKey(Upload, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=500, null=True)
    email = models.EmailField(max_length=500, null=True)
    comment = models.TextField(max_length=100000, null=True)
    date = models.DateField(auto_now_add=True, null=True)