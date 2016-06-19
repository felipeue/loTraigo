"""
All the models for our loTraigo application
Currently we support the following 6 views:

1. **UserLt** - loTraigo's User model
2. **Flight** - Flight of user
3. **Quotation** - Quotation of products
4. **Publication** - Publication of transaction betwen Buyer and Traveler
5. **Product** - Details of product
6. **Sale** - Datails of sale realised
"""

# === Imports ===
from __future__ import unicode_literals
from django.contrib.auth.models import User
# Import Country field for models
from django_countries.fields import CountryField
from django.db import models


# === User loTragio ===
class UserLt(models.Model):
    userOrigin = models.OneToOneField(User)
    address = models.CharField(max_length=128)
    phone = models.CharField(max_length=20)
    rut = models.CharField(max_length=10, unique=True)

    def __unicode__(self):
        return self.userOrigin.username


# === Flight ===
class Flight(models.Model):
    traveller = models.ForeignKey(UserLt)
    origin = CountryField(max_length=2)
    destiny = CountryField(max_length=2)
    dateFly = models.DateField()
    dateReturn = models.DateField()

    def __unicode__(self):
        return unicode(self.id)


# === Quotation ===
class Quotation(models.Model):
    userLtQ = models.ForeignKey(UserLt)
    orderNumber = models.IntegerField(unique=True)
    totalPrice = models.IntegerField()
    date = models.DateTimeField()
    description = models.TextField(max_length=1000)

    def __unicode__(self):
        return str(self.orderNumber)


# === Publication ===
class Publication(models.Model):
    quotation = models.ForeignKey(Quotation)
    state = models.BooleanField(default=False)
    benefit = models.IntegerField()

    def __unicode__(self):
        return unicode(self.id)


# === Product ===
class Product(models.Model):
    quotation = models.ForeignKey(Quotation)
    price = models.IntegerField()
    priceTotal = models.IntegerField()
    url = models.URLField()
    urlImage = models.URLField()
    title = models.CharField(max_length=500)
    category = models.CharField(max_length=500)
    widthProduct = models.IntegerField()
    weigthProduct = models.IntegerField()
    lengthProduct = models.IntegerField()
    heigthProduct = models.IntegerField()
    location = models.CharField(max_length=500)

    def __unicode__(self):
        return unicode(self.id)


# === Sale ===
class Sale(models.Model):
    quotation = models.ForeignKey(Quotation)
    numberSale = models.IntegerField(unique=True)
    date = models.DateTimeField()
    traveller = models.ForeignKey(UserLt)

    def __unicode__(self):
        return unicode(self.id)
