from django.shortcuts import render

from item.models import Category, Item
def index(request):
    items =  Item.objects.filter(is_collected=False)[0:5]
    Categories = Category.objects.all()
    return render(request, 'core/index.html',{
        'categories': Categories,
        'items': items,
    })

def contact(request):
    return render(request,'core/contact.html')