from django.http import HttpResponse
from django.shortcuts import render, redirect
from lists.models import Item, List

KEY_ENTER = b'\xEE\x80\x87'.decode()
# Create your views here.
def home_page(request):    
    return render(request, 'home.html')

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list': list_})

def new_list(request):
    list_ = List.objects.create()
    trimmedInput = request.POST['item_text'].rstrip(KEY_ENTER)
    item = Item.objects.create(text=trimmedInput, list=list_)
    try:
        item.full_clean()
    except:
        error = "You can't have an empty list item"
        return render(request, 'home.html', {'error': error})
    return redirect('/lists/%d/' % (list_.id,))

def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    trimmedInput = request.POST['item_text'].rstrip(KEY_ENTER)
    Item.objects.create(text=trimmedInput, list=list_)
    return redirect('/lists/%d/' % (list_.id,))