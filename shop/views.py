from django.shortcuts import render
from django.http import HttpResponse 
from .models import rewrite, Categories
# Create your views here.

def index(request):

    # dest1 = rewrite()
    # dest1.name = 'Laser Light'
    # dest1.desc = 'A laser produces a very narrow beam of light that is useful in many technologies and instruments. The letters in the word laser stand for Light Amplification by Stimulated Emission of Radiation.'
    # dest1.img = 'feature_prod_01.jpg'
    # dest1.price = 700
    # dest1.review = 50
    # dest1.rate = False

    # dest2 = rewrite()
    # dest2.name = 'Cloud Nike Shoes'
    # dest2.desc = 'Aenean gravida dignissim finibus. Nullam ipsum diam, posuere vitae pharetra sed, commodo ullamcorper.'
    # dest2.img = 'feature_prod_02.jpg'
    # dest2.price = 900
    # dest2.review = 59
    # dest2.rate = True

    # dest3 = rewrite()
    # dest3.name = 'Old Camera'
    # dest3.desc = 'Curabitur ac mi sit amet diam luctus porta. Phasellus pulvinar sagittis diam, et scelerisque ipsum lobortis nec.'
    # dest3.img = 'feature_prod_03.jpg'
    # dest3.price = 1900
    # dest3.review = 99
    # dest3.rate = True

    # dests = [dest1, dest2, dest3]

    # cat1 = Categories()
    # cat1.name = 'Watches'
    # cat1.img = 'category_img_01.jpg'
    
    # cat2 = Categories()
    # cat2.name = 'Shoes'
    # cat2.img = 'category_img_02.jpg'
    
    # cat3 = Categories()
    # cat3.name = 'Accessories'
    # cat3.img = 'category_img_03.jpg'
    # cats = [cat1, cat2, cat3]
    
    dests = rewrite.objects.all()
    cats = Categories.objects.all()

    return render(request, 'index.html', {'dests': dests, 'cats': cats}) 