from django.http import HttpResponse
from django.shortcuts import render, redirect
from lists.models import Item, List

KEY_ENTER = b'\xEE\x80\x87'.decode()
# Create your views here.
def home_page(request):    
    return render(request, 'home.html')

def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})

def new_list(request):
    list_ = List.objects.create()
    trimmedInput = request.POST['item_text'].rstrip(KEY_ENTER)
    Item.objects.create(text=trimmedInput, list=list_)
    return redirect('/lists/the-only-list-in-the-world/')