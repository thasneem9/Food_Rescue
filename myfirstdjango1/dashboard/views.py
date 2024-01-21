from django.shortcuts import render
from django.shortcuts import render
from item.models import Item

def index(request):
    items= Item.object.filter(created_by=admin)
    return render(request, 'dashboard/index.html',{
        'items': items,
    })