from django.shortcuts import render
from amazon.api import AmazonAPI
from django.http import HttpResponse


def index(request):
    amazon = AmazonAPI('AKIAIYBKV2XTJIHFPCXQ', 'ipwqJAnuEiIv89t5OZEttmvrKb6X1qa+TwisgExh', 'lotraigo-21')
    product = amazon.lookup(ItemId="B0051QVF7A")
    p = product.offer_url
